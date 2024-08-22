import random

'''
  Write a program that generates a random number in a given range, 
  and shows the answer to a user, 
  ask a user for the left and right border.
'''


left_number_str = input('Please, input left number: ')
right_number_str = input('Please, input right number: ')
while True: 
    if left_number_str.isdigit() and right_number_str.isdigit():
        left_n = int(left_number_str)
        right_n = int(right_number_str)
        rand_n = random.randint(left_n, right_n) if left_n < right_n else random.randint(right_n, left_n)
        print(rand_n)
        break
    elif left_number_str.isdigit():
        right_number_str = input('Please, input right number: ')
    elif right_number_str.isdigit():
        left_number_str = input('Please, input left number: ')
    else:
        left_number_str = input('Please, input left number: ')
        right_number_str = input('Please, input right number: ')