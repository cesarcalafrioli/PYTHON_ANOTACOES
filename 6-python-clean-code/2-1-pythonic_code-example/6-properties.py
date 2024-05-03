

"""
All of the properties and functions of an object are public in Python,
which is different from other languages where properties can be public,
private, or protected.
"""
class Connector:
        def __init__(self, source):
                self.source = source
                self._timeout = 60
        
        def connect(self):
            print("Connecting with {0}s".format(self._timeout))

conn = Connector("postgresql://localhost")
print(conn.source)

# Attributes that starts with an underscore must be respected as private and
# not be called externally.
print(conn._timeout)

print("\nListing all variables:")
print(conn.__dict__)

print("\nListing all variables using vars():")
print(vars(conn))

# In Python, sometimes we can encapsulate these setter and getter methods
# more compactly by using properties.
class Coordinate:
    def __init__(self, lat: float, long: float) -> None:
          self._latitude = self._longitude = None
          self.latitude = lat
          self._longitude = long
    
    @property
    def latitude(self) -> float:
          return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
            if lat_value not in range(-90, 90 + 1):
                raise ValueError(f"{lat_value} is an invalid value")
            self._latitude = lat_value
    
    @property
    def longitude(self) -> float:
        return self._longitude
    
    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-180, 180 + 1):
            raise ValueError(f"{long_value} is an invalid value")
        self._longitude = long_value
