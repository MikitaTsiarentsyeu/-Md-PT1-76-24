# 2.Write a program that calculates the area of a circle given its radius, ask a user for the radius.
import math

radius = float(
    input("Enter radius value : "))

area = round(math.sqrt(
    math.pi * radius), 2)

print("Area of the circle : ", area)
