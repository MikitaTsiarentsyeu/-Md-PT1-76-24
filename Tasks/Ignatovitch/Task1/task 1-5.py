import random
left_border = int(input("Please enter the left border of the range:"))
right_border = int(input("Please enter the right border of the range:"))
random_number = random.randint (left_border, right_border)
print(f"The random number between {left_border} and {right_border} is", random_number)