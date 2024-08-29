# 5.Write a program that generates a random number in a given range, and shows the answer to a user, ask a user for
# the left and right border.
import random

inp_type = input("Choose type float or int : ")
if inp_type == "float":
    left_border = float(input("Enter float left value : "))
    right_border = float(input("Enter float right value : "))
    rand_number_float = round(random.uniform(float(left_border), float(right_border)), 2)
    print("Random number float:", rand_number_float)

if inp_type == "int":
    left_border_int = int(input("Enter int left value : "))
    right_border_int = int(input("Enter int right value : "))
    rand_number_int = random.randint(int(left_border_int), int(right_border_int))
    print("Random number int:", rand_number_int)
