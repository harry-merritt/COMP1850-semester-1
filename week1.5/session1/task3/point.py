# Week 1.5, Session 1: Task 3

from math import sqrt


class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    # Add constructor here

    def distance(self) -> float:
        return sqrt(self.x**2 + self.y**2)
    # Add distance() method here

    # Add distance_to() method here
    # (This will need a parameter representing another point)

    def distance_to(self, p2) -> float:
        return sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

# Finally, add code here to demonstrate use of Point

p1 = Point(1,2)
p2 = Point(4,5)

print(p1.distance_to(p2))
