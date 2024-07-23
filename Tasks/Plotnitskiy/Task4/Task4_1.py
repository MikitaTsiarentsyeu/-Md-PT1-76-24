import os

if not os.path.exists("text.txt"):
    print("File 'text.txt' not found")
else:
    with open("text.txt", "r") as f:
        text = f.read()

    max_chars = int(
        input(
            "Enter the maximum number of characters per line as a number (more than 35):\n"
        )
    )

    while max_chars <= 35:
        max_chars = int(input("Enter a number greater than 35:\n"))

    paragraphs = text.split("\n")

    new_text = []

    for paragraph in paragraphs:
        words = paragraph.split()

        line = []
        line_length = 0

        for word in words:
            if line_length + len(word) + len(line) <= max_chars:
                line.append(word)
                line_length += len(word)
            else:
                extra_spaces = max_chars - line_length
                while extra_spaces > 0:
                    for i in range(len(line) - 1):
                        if extra_spaces == 0:
                            break
                        line[i] += " "
                        extra_spaces -= 1
                new_text.append("".join(line))
                line = [word]
                line_length = len(word)

        new_text.append(" ".join(line))

    with open("new_file.txt", "w") as f:
        f.write("\n".join(new_text))

    print("The text was successfully formatted and written to the file 'new_file.txt'")
