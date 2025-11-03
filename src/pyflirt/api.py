import random
from typing import List, Optional
from .data import BANK, COMPLIMENT_TEMPLATES, categories as _categories
from typing import cast, Dict


__all__ = ["line", "lines", "categories"]

def categories() -> List[str]:
    """Return a sorted list of all available pickup line categories."""
    return _categories()

def _check_cat(cat: Optional[str]) -> Optional[str]:
    if cat is None:
        return None
    if cat not in BANK:
        valid = ", ".join(_categories())
        raise ValueError(f"Unknown category {cat!r}. Choose from {valid}.")
    return cat

def _pool(cat: Optional[str], cheese: int) -> List[dict]:
    """Return candidate lines filtered by category and cheese.
    If filtering wipes everything out, fall back to the unfiltered pool.
    """
    def ok(e: dict) -> bool:
        return e.get("cheese", 3) <= cheese

    if cat is None:
        picks = [e for items in BANK.values() for e in items if ok(e)]
    else:
        picks = [e for e in BANK[cat] if ok(e)]

    if not picks:
        picks = BANK[cat] if cat else [e for items in BANK.values() for e in items]
    return picks

def _with_name(text: str, name: Optional[str]) -> str:
    if "{name}" in text:
        return text.replace("{name}", name or "you")
    return text

def line(
    category: Optional[str] = "nerdy",
    name: Optional[str] = None,
    cheese: int = 2,
    seed: Optional[int] = None,
) -> str:
    """Return one random pickup line for the given category, name, and cheese level."""
    if not 1 <= int(cheese) <= 5:
        raise ValueError("cheese must be in 1..5")
    category = _check_cat(category)
    rng = random.Random(seed)
    choice = rng.choice(_pool(category, cheese))
    return _with_name(choice["text"], name)

def lines(
    n: int = 5,
    category: Optional[str] = None,
    name: Optional[str] = None,
    cheese: int = 2,
    seed: Optional[int] = None,
) -> List[str]:
    """Return a list of n pickup lines matching the given category and cheese level."""
    if n <= 0:
        return []
    if not 1 <= int(cheese) <= 5:
        raise ValueError("cheese must be in 1..5")
    category = _check_cat(category)
    rng = random.Random(seed)
    pool = _pool(category, cheese)

    out: List[str] = []
    if len(pool) >= n:
        for e in rng.sample(pool, n):
            out.append(_with_name(e["text"], name)) # type: ignore[index]
        return out

    for _ in range(n):
        e = rng.choice(pool)
        out.append(_with_name(e["text"], name))
    return out

def compliment(role="developer", mood="sweet", name=None, emojis=0, seed=None):
    """Return a list of n pickup lines matching the given category and cheese level."""
    rng = random.Random(seed) if seed is not None else random

    role = role.lower()
    mood = mood.lower()
    if role not in COMPLIMENT_TEMPLATES:
        raise ValueError(f"Unknown role '{role}'. Choose from {list(COMPLIMENT_TEMPLATES.keys())}.")
    if mood not in COMPLIMENT_TEMPLATES[role]:
        raise ValueError(f"Unknown mood '{mood}'. Choose from {list(COMPLIMENT_TEMPLATES[role].keys())}.")

    template = rng.choice(COMPLIMENT_TEMPLATES[role][mood])
    name_bit = f", {name}" if name else ""
    text = template.format(name_bit=name_bit)

    if emojis > 0:
        text += " " + "💖" * emojis
    return text

def rate_line(text: str, metric: str = "length", seed: Optional[int] = None) -> float:
    """
    Rate a pickup line by various simple heuristics.

    Args:
        text (str): The pickup line to rate.
        rating metric (str):
            - "length": rates based on length, shorter lines get higher rating.
            - "cheese_level": rates "cheesiness" by counting cheesy words (example).
            - "random": returns a random rating for fun.
        seed (Optional[int]): Seed for random generator if metric is random.

    Returns:
        float: The rating score, higher means better according to metric.

    Raises:
        ValueError: If an unknown metric is passed.
    """
    if metric not in ("length", "cheese_level", "random"):
        raise ValueError(f"Unknown metric {metric!r}")

    if metric == "length":
        # Shorter lines score higher, normalized to length 1 to 100 chars
        length = len(text)
        rate = max(0, 100 - length)
        return float(rate)

    if metric == "cheese_level":
        # Simple cheese count by presence of known "cheesy" words
        cheesy_words = ["love", "heart", "cute", "sweet", "charm", "kiss"]
        count = sum(word in text.lower() for word in cheesy_words)
        return float(count)

    if metric == "random":
        rng = random.Random(seed)
        return rng.uniform(0, 10)
