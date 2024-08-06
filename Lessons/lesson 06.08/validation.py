SEMICOLUMN = ':'
INPUT_TIME_ASK = "Enter the time value in the hh:mm format\n"
INCORRECT_LENGTH = "Please check the lenght of your time value and try again"
CHECK_SEMICOLUMN = "Please check the semicolumn position and try again"
CHECK_NUMBERS = "Please check the numbers in your time value and try again"
CHECK_HOURS = "The hours value shoud be in range from 0 to 23, please try again"
CHECK_MINUTES = "The minutes value shoud be in range from 0 to 59, please try again"


def main():
    time_val = ask_for_time()
    tell_time(time_val)


def ask_for_time():
    while True:
        time_val = input(INPUT_TIME_ASK)

        try:
            validate_time(time_val)
        except RuntimeError as e:
            print(e)
            continue
        

        break

    return time_val

def validate_time(time_val):

        if len(time_val) != 5:
            raise RuntimeError(INCORRECT_LENGTH)
        
        if time_val[2] != SEMICOLUMN or time_val.count(SEMICOLUMN) > 1:
             raise RuntimeError(CHECK_SEMICOLUMN)
        
        hours, minutes = time_val.split(SEMICOLUMN)

        hours_error = False
        minutes_error = False

        try:
            hours = int(hours)
        except ValueError:
            hours_error = True

        try:
            minutes = int(minutes)
        except ValueError:
            minutes_error = True
        
        if hours_error and minutes_error:
            raise RuntimeError(f"{CHECK_NUMBERS} (minutes and hours error)")
        elif hours_error:
            raise RuntimeError(f"{CHECK_NUMBERS} (hours error)")
        elif minutes_error:
            raise RuntimeError(f"{CHECK_NUMBERS} (minutes error)")
        

        if hours < 0 or hours > 23:
            raise RuntimeError(CHECK_HOURS)
        
        if minutes < 0 or minutes > 59:
            raise RuntimeError(CHECK_MINUTES)

def tell_time(time_val):
    print(f"the time is {time_val}")


main()