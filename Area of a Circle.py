# Write a function to compute the area of a circle rounded off to two decimal places.
# Instructions
# The area ofa circle is calculated using the formula pi * radius^2.

import math


def calculate_area(radius):
    return round(math.pi * radius**2, 2)
