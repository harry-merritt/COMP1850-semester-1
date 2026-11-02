# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""
from __future__ import annotations

import abc
import math

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!

class Shape(abc.ABC):
    """
    An abstract base class for 2D shapes with a perimeter and area.
    """

    @abc.abstractmethod
    def perimeter(self) -> float:
        """
        Returns the perimeter of the shape.
        """

    @abc.abstractmethod
    def area(self) -> float:
        """
        Returns the area of the shape.
        """


class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x : int, y : int) -> None:
        """
        Creates a new point, with an x and y coordinate.
        """
        self.x = x
        self.y = y

    def distance(self) -> float:
        """
        Returns the distance of the point from the origin.
        """
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, p2 : Point) -> float:
        """
        Returns the distance of the point from another point.
        """
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

class Circle(Shape):
    """
    A class representing a circle, defined by a radius and centre
    """
    def __init__(self, radius : float, centre : Point | None) -> None:
        """
        Creates a new circle using a radius and centre point. If no centre is specified it defaults to (0,0).
        """
        self.radius = radius
        if centre == None:
            self.centre = Point(0,0)
        else:
            self.centre = centre

    def perimeter(self) -> float:
        """
        Returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def area(self) -> float:
        """
        Returns the area of the circle.
        """
        return math.pi * (self.radius)**2
