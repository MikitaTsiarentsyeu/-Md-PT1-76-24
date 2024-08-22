def count_words(input_string):
    """Count words with using dictionary"""
    words = input_string.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def main():
    try:
        input_string = input("Enter a string: ")
        word_count = count_words(input_string)
        print("Word count dictionary:")
        for word, count in word_count.items():
            print(f"{word}: {count}")

    except KeyboardInterrupt:  # CTRL + C for Stop
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
