import pytest

from usermanager import UserManager

@pytest.fixture
def usermanager():
    """Create a fresh instance of UserManager before each test"""
    return UserManager()

def test_add_user(usermanager):
    assert usermanager.add_user(username="Lakshan", email="lakshan@mail.com") == True
    assert usermanager.get_user(username="Lakshan") == "lakshan@mail.com"

def test_add_duplicate_user(usermanager):
    assert usermanager.add_user(username="Lakshan", email="lakshan@mail.com") == True
    with pytest.raises(ValueError, match="User already exists !!!"):
        usermanager.add_user(username="Lakshan", email="lakshan@mail.com")

def test_get_user(usermanager):
    assert usermanager.add_user(username="Lakshan", email="lakshan@mail.com")
    assert usermanager.get_user(username="Lakshan") == "Lakshan"
    assert usermanager.get_user(username="Lakshan") == "lakshan@mail.com"