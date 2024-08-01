# def oper(sign):

#     if sign == '+':
#         def operation(a, b):
#             return a+b
#     elif sign == '-':
#         def operation(a, b):
#             return a-b
#     else:
#         def operation(a, b):
#            return str(a)+str(b)   
    
#     return operation


# my_sum = oper('+')
# my_sub = oper('-')

# print(my_sum(3, 2), my_sub(3, 2))

# print(oper('+')(1, 1))


def power_maker(q):

    def action(n):
        res = n**q
        return res
    
    return action

sq = power_maker(2)
cube = power_maker(3)

print(sq(2), cube(2))

print(sq(3))




def make_logger(level, file_name=False):

    # FILE_NAME = "log.txt"

    def logger(message):
        message = f"{level}: {message}\n"
        if file_name:
            with open(file_name, 'a') as f:
                f.write(message)
        else:
            print(message)


    return logger

warning_file_logger = make_logger("WARNING", "warning.log.txt")
error_file_logger = make_logger("ERROR", "error.log.txt")

warning_file_logger("some warning")
error_file_logger("some error")

warning_console_logger = make_logger("WARNING")
error_console_logger = make_logger("ERROR")

warning_console_logger("some warning")
error_console_logger("some error")
