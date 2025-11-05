# pyflirt

[![CI](https://github.com/swe-students-fall2025/3-python-package-team_quartz/actions/workflows/ci.yml/badge.svg)](https://github.com/swe-students-fall2025/3-python-package-team_quartz/actions/workflows/ci.yml)

A small Python package with developer‑themed pickup lines and compliments. Nothing serious—just something light to play with while practicing packaging, testing, and CI.

## What is this?

This package has a collection of cheesy (but configurable) pickup lines and compliments for developers, designers, managers, and data scientists. You can get random lines, filter by category, adjust the cheesiness level, and customize compliments.

## Installation

```bash
pip install pyflirt
```

## Quick Start

```python
from pyflirt import line, lines, compliment, categories

# Get one random pickup line
print(line())

# Get a line in a specific category
print(line(category="nerdy"))

# Get multiple lines
print(lines(n=5, category="cs"))

# Get a compliment
print(compliment(role="developer", mood="sweet"))
```

## Demo program

Run the example that showcases all functions (`categories`, `line`, `lines`, `compliment`, `search`, `stats`, `stylize`, `say`, `rate_line`, `rainbow`, `ascii_heart`):

```bash
# from the repo root
PYTHONPATH=src python examples/demo.py

# or with pipenv
pipenv run python -c "import sys; sys.path.insert(0, 'src'); import examples.demo as d; d.main()"
```

## Functions

### `line(category="nerdy", name=None, cheese=2, seed=None)`

Returns one random pickup line.

- `category`: Pick a category like "nerdy", "cs", "math", "poetic", or "classic". Default is "nerdy".
- `name`: If the line supports it, this name will be inserted.
- `cheese`: How cheesy should it be? 1 (least cheesy) to 5 (very cheesy). Default is 2.
- `seed`: Optional number for reproducible results.

Example:
```python
line(category="cs", name="Alex", cheese=2)
```

### `lines(n=5, category=None, name=None, cheese=2, seed=None)`

Returns a list of pickup lines.

- `n`: How many lines you want.
- Other parameters work the same as `line()`.

Example:
```python
lines(n=3, category="math", cheese=3)
```

### `compliment(role="developer", mood="sweet", name=None, emojis=0, seed=None)`

Returns a compliment for a specific role.

- `role`: Choose from "developer", "designer", "manager", or "data".
- `mood`: "sweet", "cheeky", or "nerdy".
- `name`: Optional name to include in the compliment.
- `emojis`: Number of heart emojis to add (0-5).
- `seed`: Optional number for reproducible results.

Example:
```python
compliment(role="designer", mood="cheeky", name="Sam", emojis=2)
```

### `categories()`

Returns a list of all available pickup line categories.

Example:
```python
print(categories())
# ['classic', 'cs', 'math', 'nerdy', 'poetic']
```

### `search(query, category=None, name=None, cheese=5, limit=10, seed=None)`

Find up to `limit` lines containing `query` (case-insensitive), optionally filtered.

- `query`: substring to match (required)
- `category`: filter by category or search all
- `name`: optional replacement for `{name}` placeholders
- `cheese`: 1–5 max cheese allowed in results
- `limit`: max results to return
- `seed`: for deterministic ordering

Example:
```python
search("code", category="cs", limit=3, seed=7)
```

### `stats()`

Return counts for available lines.

Returns a dict with keys: `total`, `by_category`, and `cheese_hist`.

Example:
```python
s = stats()
print(s["total"], s["by_category"], s["cheese_hist"])
```

### `stylize(text, width=None, uppercase=False, color="auto")`

Format a string with optional wrapping, uppercasing, and ANSI color.

- `width`: wrap to this many columns (None = no wrap)
- `uppercase`: True to uppercase the text
- `color`: one of `"auto"`, `"none"`, `"magenta"`, `"cyan"`, `"green"`

Example:
```python
stylize("hello world", width=8, uppercase=True, color="none")
```

### `say(category="nerdy", name=None, cheese=2, seed=None, width=None, uppercase=False, color="auto", emojis=0)`

Generate a line, decorate it (wrap/case/color/emojis), print it, and return it.

Example:
```python
say(category="nerdy", seed=1, width=16, color="none", emojis=2)
```

### `rate_line(text, metric="length"|"cheese_level"|"random", seed=None)`

Score a line by the chosen metric.

- `length`: higher for shorter lines (simple heuristic)
- `cheese_level`: counts cheesy keywords
- `random`: seeded 0–10 score

Example:
```python
rate_line("You are so sweet", metric="cheese_level")
```

### `rainbow(text)`

Colorize text with rainbow ANSI codes 🌈
Useful for terminals that support color formatting.

Example:
```python
print(rainbow("You light up my console! 💻"))
```

### `ascii_heart()`

Return a multi-line ASCII heart ❤️. A great decoration after a compliment.

Example:
```python
print(ascii_heart())
```
## Development Setup

If you want to work on this package:

1. Clone the repo:
```bash
git clone https://github.com/swe-students-fall2025/3-python-package-team_quartz.git
cd 3-python-package-team_quartz
```

2. Install pipenv (if you don't have it):
```bash
pip install pipenv
```

3. Install dependencies:
```bash
pipenv install --dev
```

4. Activate the virtual environment:
```bash
pipenv shell
```

5. Run tests:
```bash
pytest
```

6. Build the package:
```bash
python -m build
```

## Links

- [PyPI Package](https://pypi.org/project/pyflirt/0.1.0/)
- [TestPyPI (0.1.0)](https://test.pypi.org/project/pyflirt/0.1.0/)
- [GitHub Repository](https://github.com/swe-students-fall2025/3-python-package-team_quartz)

## Contributors

Team
- Siqi Zhu — [@HelenZhutt](https://github.com/HelenZhutt)
- Daniel Lee - [@danielleesignup](https://github.com/danielleesignup)
- Sam Murshed - [@Sammurshed] (https://github.com/SamMurshed)
- Matthew Viola
- Jordan Lee - [@jjl9930] (https://github.com/jjl9930)


More links
- [Contributors Graph](https://github.com/swe-students-fall2025/3-python-package-team_quartz/graphs/contributors)
- [Commits](https://github.com/swe-students-fall2025/3-python-package-team_quartz/commits)

