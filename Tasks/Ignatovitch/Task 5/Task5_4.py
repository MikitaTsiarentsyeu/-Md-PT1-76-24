def letter_counter(string):
    lower_case = 0
    upper_case = 0
    for letter in string:
        if letter.islower():
            lower_case +=1
        elif letter.isupper():
            upper_case +=1
    return(lower_case, upper_case)    

print(letter_counter("Caroline and mum"))    