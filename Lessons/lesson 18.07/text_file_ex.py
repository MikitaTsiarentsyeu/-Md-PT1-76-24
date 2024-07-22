with open("text_file_ex.txt", 'r') as f:
    with open("text_file_ex_formatted.txt", 'w') as f_new:
        f_new.write(f.read().replace('!', '.').replace('?', '.').replace(',', '.'))


with open("text_file_ex.txt", 'r') as f:
    with open("text_file_ex_formatted.txt", 'w') as f_new:
        for line in f:
            f_new.write(line.replace('!', '.').replace('?', '.').replace(',', '.'))