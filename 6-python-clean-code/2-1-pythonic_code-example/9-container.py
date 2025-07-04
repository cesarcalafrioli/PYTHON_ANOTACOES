### Container objects
"""
Containers are objects that implement a __contains__ method, which usually
returns a Boolean value. This method is called in the presence of the in
keyword of Python.
"""
# Ex:
# element in container -> container.__contains__(element)

class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height
    
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    def __contains__(selof, coord):
        return coord in self.limits