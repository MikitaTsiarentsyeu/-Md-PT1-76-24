#1. Prepare to read the contents of the file text.txt
#2. Allow the user to enter a parameter "maximum number of characters per line", which must be greater than 35.
#3. Format the text taking into account the maximum number of characters, but if a word does not fit entirely on a line, it should be moved to the next one, and the spacing between words should be evenly increased (similarly to the "Justify" function in text editors). There is a module called ‘textwrap’ which can do it, you may take a look at it but do not use for this task.
#4. Write the resulting text to a new file and notify the user about it.

import os
maximum_number = int(input("Maximum number of characters per line(more than 35): "))

#validation
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, "text2.txt")
file_path = r"C:\course\-Md-PT1-76-24\Tasks\Mihailova\task4\text1.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()
current_line = ""
formatted_text = ""

for word in words:
    if len(current_line) + len(word) + 1 > maximum_number:
        formatted_text += current_line + "\n"
        current_line = word
    else:
        if current_line:
            current_line += " "
        current_line += word

if current_line:
    formatted_text += current_line

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(formatted_text)
print(f"Отформатированный текст был сохранен в '{output_file}'")
