VALIDATION_MSG_1 = "incorrect length of inputted value, please try again"
VALIDATION_MSG_2 = "incorrect format of inputted value, please try again"

while True:

    user_input = input("input your value in format hh:mm\n")

    if len(user_input) != 5:
        print(VALIDATION_MSG_1)
        continue

    if user_input[2] != ':' or user_input.count(':') != 1:
        print(VALIDATION_MSG_2)
        continue

    hours, minutes = user_input.split(':')
    if not (hours.isdigit() and minutes.isdigit()):
        print(VALIDATION_MSG_2)
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 23 or minutes > 59:
        print(VALIDATION_MSG_2)
        continue

    break

print("the end")
