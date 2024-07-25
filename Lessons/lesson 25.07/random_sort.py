import random

l = [3,5,7,8,6,43,2,42]

def random_sort(l:list) -> int:
    
    count = 0

    while not is_sorted(l):
        n = len(l)-1
        i = generate_index(n)
        j = i
        while j == i:
            j = generate_index(n)
        
        swap(l, i, j)
        count += 1

    return count

def is_sorted(l:list) -> bool:
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def generate_index(n:int) -> int:
    return random.randint(0, n)

def swap(l:list, i:int, j:int) -> None:
    l[i], l[j] = l[j], l[i]

print(random_sort(l))
print(l)