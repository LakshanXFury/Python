import pytest

from main import add, get_weather, divide

def test_add():
    assert add(2, 3) == 5, "2 + 3 should be 5"

def test_add_fail():
    assert add(2, 3) == 10, "2 + 3 should be 5, if 10 it should fail"

def test_get_weather():
    assert get_weather(21) == "hot"

# Raise Error
def test_divide():
    """pytest.raises is a context manager that lets you test whether your code raises a specific exception as expected."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10,0)