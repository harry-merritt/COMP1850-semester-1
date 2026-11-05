# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from point import Point
from shapes import Circle

circ = Circle(Point(2,5), "red", 2.5)
print(circ)

print(round(circ.area(),3),round(circ.perimeter(),3))
circ.set_position(Point(3,2))
circ.set_colour("blue")
print(circ)
