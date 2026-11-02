# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

from geometry import Circle, Point

x = int(input("Please enter an x coordinate for the centre point "))
y = int(input("Please enter a y coordinate for the centre point "))

point = Point(x,y)

radius = float(input("Please enter a circle radius "))

circ = Circle(radius, point)

print(f"The area of the circle is {round(circ.area(),4)}")
print(f"The perimeter of the circle is {round(circ.perimeter(),4)}")
