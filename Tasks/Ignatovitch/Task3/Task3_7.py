user_input = input("Enter a string:\n")

result = ""

for letter in user_input:
   if letter.isupper():
        result += letter.lower()
   else:
        result += letter.upper()
        
print("Converted string:", result)