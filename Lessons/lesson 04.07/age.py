import datetime

print(datetime.datetime.now())

current_year = datetime.datetime.now()

print(current_year)

age = input("Please, enter your age (digits only):")

if age.isdigit():

    if len(age) > 3:
        print("please use at most 3 digits next time")
        exit()

    age = int(age)
    print(age)

    if age > 125:
        print("please use a value less than 125")
        exit()

else:
    print("please use only digits next time")
    exit()

yob = current_year - age
print(yob)


dob = input("please enter your data of birth in format dd.mm.yyyy:")
dob.isdigit()

if dob.count('.') == 2:

    d, m, y = dob.split('.')
    print(d, m, y)

else:
    print("please stick to the dd.mm.yyyy format next time")
    exit()