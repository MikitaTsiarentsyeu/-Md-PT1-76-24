"""
1. Prepare to read the contents of the file text.txt
2. Allow the user to enter a parameter "maximum number of characters per line", which must be greater than 35.
3. Format the text taking into account the maximum number of characters, but if a word does not fit entirely on a line,
it should be moved to the next one, and the spacing between words should be evenly increased (similarly to the "Justify"
function in text editors). There is a module called ‘textwrap’ which can do it,
you may take a look at it but do not use for this task.
4. Write the resulting text to a new file and notify the user about it.

General concept:
From the text we make a list of words "list_text".
We create an intermediate line, “limited_line”,
go through the list “list_text” and concatenate each word to the limit,
then add spaces and add “finish_line” to the main line, start a new line “limited_line”.
We add the main line "finish_line" to the list. "first_list".
"""
import os

if os.name == 'posix':
    way = '/home/arty/PycharmProjects/-Md-PT1-76-24/Tasks/!!!Tasks/Task4/text.txt'
elif os.name == 'nt':
    way = r'F:\python\repository\-Md-PT1-76-24\Tasks\!!!Tasks\Task4\text.txt'

list_text = []

with open(way, 'r', encoding='utf-8') as file:
    for line in file:
        # read the file, write it to the list
        list_text.append(line.rstrip().split(' '))

while True:
    # Checking the value
    try:
        n = int(input('Enter value > 35: '))
        if n > 35:
            break
        else:
            print('You must enter a value greater than 35!')
    except:
        print('Please, enter numbers only!')

first_list = []
for line in list_text:
    limited_line = ''  # intermediate line
    finish_line = ''  # main line
    for word in line:
        # write words into the line, if the line is full then start a new one
        if len(limited_line) >= n or len(limited_line + word) >= n:
            l_b = limited_line.count(' ')  # number of spaces in line
            c = 1  # count
            remainder_symbols = n - len(limited_line)  # number of missing spaces
            while not remainder_symbols <= 0:
                # fill with spaces up to the limit number n
                c += 1  # each iteration we increase the number of spaces
                limited_line = limited_line.replace(' ' * (c - 1), ' ' * c, remainder_symbols)
                # Add more spaces if necessary
                remainder_symbols -= l_b  # remainder of spaces
            finish_line += limited_line + '\n'
            limited_line = ''
            limited_line += word
        else:
            limited_line += word if len(limited_line) == 0 else ' ' + word
            # do not add a space to the first word
    if len(limited_line) != 0:
        # concatenate the last line, no changes
        finish_line += limited_line + '\n'
    first_list.append(finish_line)

first_list[-1] = first_list[-1][0:-1]  # remove the last space

with open('text', 'w', encoding='utf-8') as file:
    for i in first_list:
        file.write(i)
    print('The file is recorded!')
