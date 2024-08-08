user_input = input("Please enter the string: \n")
vowels = 'aeiouyAEIOUY'
count = 0

for letter in user_input:
    if letter in vowels:
        count += 1

print(f"The number of vowels in the string is: {count}")