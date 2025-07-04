### Callable objects
"""
It is possible to define objects that can act as functions. Create better
decorators is one of the most common applications, but it's not limited to
that.
"""
from collections import defaultdict
class CallCount:
    def __init__(self):
        self._counts = defaultdict(int)
    
    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]

cc = CallCount()
print(cc(1))

print(cc(2))

print(cc(1))

print(cc(1))

print(cc("Something"))

print(callable(cc))