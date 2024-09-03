"""
1. Prepare to read the contents of the file text.txt
2. Allow the user to enter a parameter "maximum number of characters per line", which must be greater than 35.
3. Format the text taking into account the maximum number of characters, but if a word does not fit entirely on a line, it should be moved to the next one, and the spacing between words should be evenly increased (similarly to the "Justify" function in text editors). There is a module called ‘textwrap’ which can do it, you may take a look at it but do not use for this task.
4. Write the resulting text to a new file and notify the user about it.
"""
import os


def format_text():
    file_path = os.path.join("..", "..", "!!!Tasks", "Task4", "text.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r') as read_file:
            with open("format_text.txt", 'w') as write_file:
                for parag in read_file.read().split('\n'):
                    line = []
                    len_line = 0
                    for word in parag.split():
                        if (len_line + len(word)) < max_number:
                            line.append(word)
                            len_line += len(word) + 1
                        else:
                            spaces_to_add = max_number-len_line
                            if len(line) > 1:
                                for i in range(spaces_to_add):
                                    line[i % (len(line) - 1)] += ' '
                            write_file.writelines(f'{" ".join(line)}\n')                    
                            line = [word]
                            len_line = len(word) + 1
                    if len_line:
                        write_file.writelines(f'{" ".join(line)}\n')

try:
    max_number = int(input("Input maximum number of characters per line (>35): "))
    if max_number < 35:
        print("Invalid number")
    else:
        format_text()  
except ValueError:
    print('Not a number, please retry!')

