"""
1. Prepare to read the contents of the file text.txt
2. Allow the user to enter a parameter "maximum number of characters per line", which must be greater than 35.
3. Format the text taking into account the maximum number of characters, but if a word does not fit entirely on a line,
   it should be moved to the next one, and the spacing between words should be evenly increased (similarly to the
   "Justify" function in text editors). There is a module called 'textwrap' which can do it, you may take a look at it
   but do not use for this task.
4. Write the resulting text to a new file and notify the user about it.
"""

import os

MIN_CHARS_PER_LINE = 35

def get_max_chars_per_line():
    while True:
        max_chars = input(f"Enter the maximum number of characters per line (must be greater than {MIN_CHARS_PER_LINE}):\n")
        if max_chars.isdigit() and int(max_chars) > MIN_CHARS_PER_LINE:
            return int(max_chars)
        print(f"Please enter a number greater than {MIN_CHARS_PER_LINE}.")

def justify_text(text, max_chars_per_line):
    words = text.split()
    formatted_lines = []
    current_line = []
    current_line_length = 0

    for word in words:
        word_length = len(word)
        if current_line_length + word_length + len(current_line) > max_chars_per_line:
            justified_line = justify_line(current_line, max_chars_per_line - current_line_length)
            formatted_lines.append(justified_line)
            current_line = [word]
            current_line_length = word_length
        else:
            current_line.append(word)
            current_line_length += word_length

    if current_line:
        justified_line = ' '.join(current_line)
        formatted_lines.append(justified_line)

    return '\n'.join(formatted_lines)

def justify_line(words, remaining_spaces):
    num_spaces = len(words) - 1
    if num_spaces == 0:
        return words[0]

    spaces_per_gap = remaining_spaces // num_spaces
    extra_spaces = remaining_spaces % num_spaces
    justified_line = []

    for i, word in enumerate(words):
        justified_line.append(word)
        if i < num_spaces:
            justified_line.append(' ' * (spaces_per_gap + (1 if extra_spaces > 0 else 0)))
            extra_spaces -= 1

    return ''.join(justified_line)

def main():
    with open("text.txt", "r") as file:
        text = file.read()

    max_chars_per_line = get_max_chars_per_line()
    justified_text = justify_text(text, max_chars_per_line)

    output_file = "justified_text.txt"
    with open(output_file, "w") as file:
        file.write(justified_text)

    print(f"Justified text has been written to {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
