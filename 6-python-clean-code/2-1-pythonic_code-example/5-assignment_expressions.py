"""
Demonstrations of assignment expressions, according with the PEP-572

Links:
https://realpython.com/lessons/assignment-expressions/#:~:text=Assignment%20expressions%20allow%20you%20to,%3E%3E%20print(walrus)%20False
https://peps.python.org/pep-0572/
"""


# Example 1 - Common code
walrus = False
print(walrus)

# Example 2 - Combining two satements above into one using walrus operator
print(walrus := True)

print(type(walrus))


# Example 3 - Common code
inputs = list()
current = input("Write something: ")
while current != "quit":
    inputs.append(current)
    current = input("Write something: ")

# Example 4 - Avoiding repetitions and keeping the lines in a more logical order
inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)
