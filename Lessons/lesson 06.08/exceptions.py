l = ["one", "two", "three"]

num = input("enter some integer number:\n")

def convert_to_int(number):
    try:
        return int(number)
    except ValueError:
        raise RuntimeError("the value you've you entered is not integer")

try:
    try:
        try:
            num = convert_to_int(num)
        except RuntimeError as e:
            print(e)
            exit()
        print(f"your number is {num}")
        print(f"your value is {l[100/num]}")
    # except ValueError:
    #     print("the value you've you entered is not integer")
    #     exit()
    except IndexError:
        print("the value you've you entered is not in the range of the collection")
        exit()
except:
    print("something went wrong")
    print("the end")





try:
    f = open("test.txt", "r")
    is_open = True
    f.read()
except FileNotFoundError:
    is_open = False
finally:
    if is_open:
        f.close()

with open("test.txt", "r") as f:
    f.read()