"""
Since Python 3.7, we can simplify this by using the dataclasses module,
which has been introduced by PEP-557

The @dataclass decorator, when applied to a class, take all the class
attributes with annotations, and treat them as instance attributes, as
if they were declared in the initialization method.

Using this decorator, it will automatically generate the __init__ method
on the class, so we don't have to.
"""
from typing import List
from dataclasses import dataclass, field

R = 26
@dataclass
class RTrieNode:
    size = R
    value: int
    next_: List["RTrieNode"] = field( default_factory=lambda: [None] * R )

    def __post_init__(self):
        if len(self.next_) != self.size:
            raise ValueError(f"Invalid length provided for next list")
