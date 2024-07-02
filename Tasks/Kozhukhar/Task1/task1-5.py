import random

left = int(input("Please enter the left border of the range: "))
right = int(input("Please enter the right border of the range: "))

random_number = random.randint(left, right)

print(f"{random_number} is random number between {left} and {right}")
