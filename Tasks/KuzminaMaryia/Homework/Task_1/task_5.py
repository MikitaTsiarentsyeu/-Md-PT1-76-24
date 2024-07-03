import random
rand = random.randint(0, 5)
print("The computer has guessed a number from 0 to 5. Guess it. You have 2 attempts")
write = int(input('Enter a number:'))
if write == rand:
    print("Well done")
elif write > rand:
    print("Too high")
    write = int(input('Guess again:'))
    if write == rand:
        print("Well done")
    else:
        print("You lose")
elif write < rand:
    print("Too low")
    write = int(input('Guess again:'))
    if write == rand:
        print("Well done")
    else:
        print("You lose")
else:
 print("You lose")
