import pytest

from  main import is_prime

""" Using this method we can test with multiple data at a time."""

@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4,False),
    (17, True),
    (18, False),
    (19, True),
    (25, False),
]) # Num and expected value to check a tuple of data to check if it matches.

def test_is_prime(num, expected):
    assert is_prime(7) == True
    assert is_prime(num) == expected