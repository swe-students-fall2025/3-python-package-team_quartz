"""
pyflirt 💘

APIs:
- line(category, name, cheese, seed)
- lines(n, categories, name, cheese, seed)
- compliment(role, mood, name, emojis, seed)
- rate_line(text, metric, seed)
"""
from .api import line, lines, categories, compliment

__all__ = [
    "compliment",
    "line",
    "lines",
    "categories",
]

__version__ = "0.1.0"
