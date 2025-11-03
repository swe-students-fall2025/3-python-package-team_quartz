from pyflirt import line, lines, categories

def test_categories_present():
    assert "nerdy" in categories()

def test_line_seed_stable():
    assert line(category="nerdy", seed=42) == line(category="nerdy", seed=42)

def test_lines_len_and_content():
    arr = lines(n=3, name="Sam", seed=123)
    assert len(arr) == 3
    assert all(isinstance(s, str) and s for s in arr)

def test_cheese_bounds():
    import pytest
    with pytest.raises(ValueError):
        line(cheese=0)
    with pytest.raises(ValueError):
        lines(n=2, cheese=6)
