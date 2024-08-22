VALIDATION_MSG_1 = "incorrect length of inputted value, please try again"
VALIDATION_MSG_2 = "incorrect format of inputted value, please try again"

while True:

    user_input = input("Введите время в формате 'hh:mm': ")

    if len(user_input) != 5:
        print(VALIDATION_MSG_1)
        continue

    if user_input[2] != ':' or user_input.count(':') != 1:
        print(VALIDATION_MSG_2)
        continue

    h, m = user_input.split(":")
    if not (h.isdigit() and m.isdigit()):
        print(VALIDATION_MSG_2)
        continue

    h = int(h)
    m = int(m)

    if h > 23 or m > 59:
        print(VALIDATION_MSG_2)
        continue

    break


