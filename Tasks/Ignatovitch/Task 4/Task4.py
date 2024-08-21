with open("text.txt", "r") as f:
    text = f.read()

while True:
    max_chars_per_line = int(input("Enter the maximum number of characters per line (must be greater than 35):\n"))
    if max_chars_per_line > 35:
        break
    print("Please enter a number greater than 35.")

words = text.split()

formatted_text = []
current_line = []

for word in words:
    if sum(len(w) for w in current_line) + len(current_line) + len(word) <= max_chars_per_line:
        current_line.append(word)
    else:
        total_spaces = max_chars_per_line - sum(len(w) for w in current_line)
        if len(current_line) > 1:
            spaces_between_words = total_spaces // (len(current_line) - 1)
            extra_spaces = total_spaces % (len(current_line) - 1)
        else:
            spaces_between_words = 0
            extra_spaces = 0
        
        justified_line = current_line[0]
        for i in range(1, len(current_line)):
            if i <= extra_spaces:
                justified_line += ' ' * (spaces_between_words + 1) + current_line[i]
            else:
                justified_line += ' ' * spaces_between_words + current_line[i]

        formatted_text.append(justified_line)
        current_line = [word]

formatted_text.append(' '.join(current_line))

output_filename = "justified_text.txt"
with open(output_filename, "w") as file:
    for line in formatted_text:
        file.write(line + "\n")

print(f"The formatted text has been written to '{output_filename}'")