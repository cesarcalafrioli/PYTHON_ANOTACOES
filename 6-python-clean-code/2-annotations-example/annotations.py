# Pep 3107 ( Annotations )-> https://peps.python.org/pep-3107/
# Pep 484 ( Type Hints ) -> https://peps.python.org/pep-0484/

from dataclasses import dataclass

 # PEP-526 and PEP-557 use for declare attribute in a class and use annotations to set their type, and
 # with the help of the @dataclass decorator. With these, it won't be needed explicity declare the __init__
 # method and set values to them
@dataclass
class Point:
    lat: float
    long: float

 # Type Hints example ( PEP 484 )
def locate(latitude: float, longitude: float) -> Point: 
    """Find an object in the map by its coordinates""" # OBS: Docstring complements annotation and vice-versa
    return None

def greeting(name: str) -> str:
    """Give a Hello message with user's name"""
    return 'Hello ' + name

print("Showing the annotations")
print(Point.__annotations__)
print(Point(1, 2))

