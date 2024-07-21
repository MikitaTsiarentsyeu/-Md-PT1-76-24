def read_file(filename):
    """Reads the contents of a file and returns it as a string."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def get_max_length():
    """Prompts the user for the maximum number of characters in a line, checking that it is greater than 35."""
    while True:
        try:
            max_length = int(
                input("Enter the maximum number of characters per line (more than 35):")
            )
            if max_length > 35:
                return max_length
            else:
                print("Error: The number must be greater than 35.")
        except ValueError:
            print("Error: Please enter a valid number.")


def justify_paragraph(paragraph, line_length):
    """Formats a paragraph based on the maximum number of characters per line, justified."""
    words = paragraph.split()
    lines = []
    current_line = []

    for word in words:
        if len(" ".join(current_line + [word])) <= line_length:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]

    if current_line:
        lines.append(" ".join(current_line))

    justified_lines = []
    for line in lines[:-1]:  # The last line is not aligned in width
        if len(line) < line_length:
            spaces_to_add = line_length - len(line)
            parts = line.split()
            if len(parts) == 1:
                justified_lines.append(line)
                continue

            spaces_between_words = len(parts) - 1
            extra_spaces = spaces_to_add // spaces_between_words
            additional_space_slots = spaces_to_add % spaces_between_words

            for i in range(additional_space_slots):
                parts[i] += " "

            justified_line = (" " * (extra_spaces + 1)).join(parts)
            justified_lines.append(justified_line)
        else:
            justified_lines.append(line)

    justified_lines.append(lines[-1])  # Add the last line without alignment

    return "\n".join(justified_lines)


def justify_text(text, line_length):
    """Formats text based on the maximum number of characters per line, justified, and preserved in paragraphs."""
    paragraphs = text.split("\n")  # Dividing text into paragraphs
    justified_paragraphs = [
        justify_paragraph(paragraph, line_length) for paragraph in paragraphs
    ]
    return "\n".join(justified_paragraphs)


def write_file(filename, content):
    """Writes the contents to the file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    input_filename = "text.txt"
    output_filename = "new_text.txt"

    text = read_file(input_filename)

    max_length = get_max_length()

    justified_text = justify_text(text, max_length)

    write_file(output_filename, justified_text)

    print(
        f"The text has been successfully formatted and written to the file {output_filename}"
    )


if __name__ == "__main__":
    main()
