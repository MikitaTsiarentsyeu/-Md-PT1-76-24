num = 12345

def digit_sum_loop(num:int, i=0, res=0):
    str_num = str(num) if isinstance(num, int) else num

    if i == len(str_num):
        return res
    
    res += int(str_num[i])
    return digit_sum_loop(str_num, i+1, res)

print(digit_sum_loop(num))


def digit_sum_rem(num):
    if num == 0:
        return 0

    return digit_sum_rem(num//10) + num % 10


print(digit_sum_rem(num))