"""
Pydantic is a data validation library for Python. Its main job is to make sure your data is the correct type and structure.

Pydantic and BaseModel make your data reliable and predictable, which is especially important when working with AI
where outputs can be unpredictable!
"""

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool

# Correct ✅
user = User(name="Lakshan", age=25, is_active=True)

# Wrong type ❌ — Pydantic throws error immediately!
# user1 = User(name="Lakshan", age="twenty five", is_active="yes")
# ValidationError: age must be an integer!

# Convert to dictionary:
print(user.model_dump())

#  Convert to JSON:
print(user.model_dump_json())


"""
Without Pydantic:         With Pydantic BaseModel:
┌─────────────────┐       ┌─────────────────┐
│ Fill anything   │       │ Name: [string]  │ ← must be string
│ in any format   │       │ Age:  [int]     │ ← must be int
│ No rules!       │       │ Active: [bool]  │ ← must be bool
└─────────────────┘       └─────────────────┘
                          Enforced! ✅
                          
"""