from main import add

def test_add():
    assert add(2, 3) == 5, "2 + 3 should be 5"

def test_add_fail():
    assert add(2, 3) == 10, "2 + 3 should be 5, if 10 it should fail"
