### Caveats to avoid
"""
"""

# Mutable default arguments
"""
Don't use mutable objects as the default arguments of functions.

This will actually only work the first time it is called without arguments.
For the second time, we call it without explicitly passing something to
user_metadata . It will fail with a KeyError
"""
print("\nMutable default arguments:")
def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"

print(wrong_user_display())
print(wrong_user_display({"name": "Jane", "age": 25}))
#print(wrong_user_display()) # Here it will return an error

# Solution -> Use None as a default sentinel value
def correct_user_display(user_metadata: dict = None):
    user_metadata = user_metadata or {"name": "John", "age": 30}
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"

print()
print(correct_user_display())
print(correct_user_display({"name": "Jane", "age": 25}))
print(correct_user_display())

# Extending built-in types
"""
At first sight, it looks like the object behaves as we want it to. But then, if
we try to iterate it (after all, it is a list ), we find that we don't get what we
wanted.
"""
print("\nExtending built-in types")
class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"

b1 = BadList((0,1,2,3,4,5))
print(b1[0])
print(b1[1])
#print("".join(b1)) # Error

# Solution -> Using UserList instead of list
from collections import UserList
class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"

print()
g1 = GoodList((0,1,2))
print(g1[0])
print(g1[1])
print(";".join(g1))
"""
OBS: Don't extend directly from dict ; use collections.UserDict
instead. For lists, use collections.UserList , and for strings, use
collections.UserString .
"""

