with open("text.txt", 'r') as text_read:
    text_txt = text_read.read()


input_leng_user = int(input("Enter number which must be greater than 35: "))

while True:
    if input_leng_user < 35: print("Enter a number greater than 35")
    if input_leng_user >= 35: break


d = text_txt.split("\n")
new_text_txt = []


for paragraph in d: 
    paragraph_split = paragraph.split() 
    line = []
    leng_line = 0
    for word in paragraph_split:
        if  leng_line + len(word) + len(line) <= input_leng_user:
            line.append(word)
            leng_line += len(word)
        else:
            add = input_leng_user - leng_line
            while add > 0:
                for f in range(len(line) - 1):
                    if add == 0: break
                    line[f] += " "
                    add -= 1
            new_text_txt.append("".join(line))
            line = [word]
            leng_line = len(word)
    new_text_txt.append("".join(line))


with open ("new_text.txt", "w") as text_read:
    text_read.write("\n".join(new_text_txt))


print("gotovo")