"""
Trainning source:
https://www.youtube.com/watch?v=yScuF1UgGU0 OBS: CONTINUAR ESTUDO NESTE VIDEO ( BINARY TREE )
Book Clean Code in Python
"""

from typing import Iterable
import logging

logger = logging.getLogger(__name__)

def broadcat_notification(
        message: str,
        relevant_user_emails: Iterable[str]
):
        for email in relevant_user_emails:
                logger.info("sending %r to %r", message, email)

broadcat_notification("welcome", "user1@domain.com")

""""
In the prompt, type "mypy mypy.py"

This is not a valid instance because it will iterate every
character in the string, and try to use it as an email. Here we have
a false positive
"""

# Test 2
def caesar(text: str, key: int) -> str:
        result: str = ""
        for char in text:
                c = ord(char)
                enc_char = chr(c + key)
                result += enc_char
        return result

print(caesar("uwduetkdg", -2))

# Test 3
class BinaryTree:
    value = int

    left: 'BinaryTree' = None
    right: 'BinaryTree' = None

    def __init__(self, value):
        self.value = value

    def add(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.add(value)

    def find(self, value):
        if self.value == value:
            return self.value
        elif value < self.value and self.left is not None:
            return self.left.find(value)
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        return None

    def traverse(self, func):
        if self.left is not None:
            if not self.left.traverse(func):
                return False

        done = not func(self.value)
        if done:
            return False

        if self.right is not None:
            if not self.right.traverse(func):
                return False

        return True


def printer(n):
    print(n)
    return True


tree = BinaryTree(5)
print(tree.find(5))
print(tree.find(4))

tree.add(4)
print(tree.find(4))

tree.add(7)
tree.add(3)
tree.add(0.5)

print("\nPrint Tree:")
tree.traverse(printer)