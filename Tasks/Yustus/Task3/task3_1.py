##  Write a program that takes a string as input from a user and returns the number of vowels in the string.
user_input = input("Please enter the string: \n")
vowels = "aeiouAEIOU"
count = 0
for char in user_input:
    if char in vowels:
        count += 1
        print(char, end=" ")
print(f"\nNumber of vowels in the string: {count}")
