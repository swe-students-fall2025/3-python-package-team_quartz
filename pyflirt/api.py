import random
from typing import List, Optional
from .data import BANK, categories as _categories

__all__ = ["line", "lines", "categories"]

def categories() -> List[str]:
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
    if not (1 <= int(cheese) <= 5):
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
    if n <= 0:
        return []
    if not (1 <= int(cheese) <= 5):
        raise ValueError("cheese must be in 1..5")
    category = _check_cat(category)
    rng = random.Random(seed)
    pool = _pool(category, cheese)

    out: List[str] = []
    if len(pool) >= n:
        for e in rng.sample(pool, n):
            out.append(_with_name(e["text"], name))
        return out

    for _ in range(n):
        e = rng.choice(pool)
        out.append(_with_name(e["text"], name))
    return out
