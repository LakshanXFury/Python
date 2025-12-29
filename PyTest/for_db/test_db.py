"""
Testing the Database Functionality
"""

import pytest
from db import Database

@pytest.fixture()
def db():
    """Create a fresh instance of Database class and cleans after the test"""
    database = Database()
    yield database # Provides the fixture instance,
    database.data.clear() # Cleanup setup ( not needed for in-memory , but useful for real DB's)


def test_add_user(db): # Here the yield works, when it is used it will work.
    db.add_user(user_id=1, name="John Wick")
    assert db.get_user(user_id=1) == "John Wick"

def test_add_duplicate_user(db):
    db.add_user(user_id=1, name="John Wick")
    with pytest.raises(ValueError, match="User already exists !!!"):
        db.add_user(user_id=1, name="John Wick")

def test_delete_user(db):
    db.add_user(user_id=1, name="John Wick")
    db.delete_user(user_id=1)
    assert db.get_user(user_id=1) is None