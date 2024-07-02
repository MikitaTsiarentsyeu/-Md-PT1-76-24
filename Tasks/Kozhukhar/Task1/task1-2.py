import math

rad = float(input("Please enter the radius to calculate the area of the circle: "))


def area_circle(rad):
    """Calculates the area of a circle from its radius"""
    return math.pi * rad**2


print(f"The area of a circle with radius {rad} is {area_circle(rad):.2f}")
