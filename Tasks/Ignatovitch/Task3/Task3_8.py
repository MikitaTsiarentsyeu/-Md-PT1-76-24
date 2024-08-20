user_input = input("Enter a list of numbers separated by spaces: ")

numbers =list(map(float, user_input.split()))

total_sum = 0
count = 0

for number in numbers:
    total_sum += number
    count += 1
    if count > 0:
        average = total_sum / count
    else:
        average = 0

print("The average of all numbers is:", average)