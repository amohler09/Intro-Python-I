# Make a class LatLon that can be passed parameters `lat` and `lon` to the constructor
# # https://docs.python.org/3/tutorial/classes.html

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon   
    

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# Super method - https://www.pythonforbeginners.com/super/working-python-super-function

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return f'{self.name}, {self.lat}, {self.lon}'

# Test if it's working
# w = Waypoint('home', 123, 456)
# print(w.name)
# print(w.lat)
# print(w.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.size = size
        self.difficulty = difficulty
    def __str__(self):
        return f'{self.name}, diff {self.difficulty}, size {self.size}, {self.lat}, {self.lon}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# Class string method https://docs.python.org/2/library/string.html
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
