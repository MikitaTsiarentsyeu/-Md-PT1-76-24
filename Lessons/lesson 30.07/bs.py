l = [1,2,3,4,5,6,7,8,9]

target = 7

pos = False
count = 0
for i in range(len(l)):
    count += 1
    if l[i] == target:
        pos = i
        break

print(pos, count)

def search(l, target, low, high, count=0):
    if low > high:
        return False

    mid = (low + high) // 2
    if l[mid] == target:
        return mid, count+1
    elif l[mid] > target:
        return search(l, target, low, mid-1, count+1)
    else:
        return search(l, target, mid+1, high, count+1)
    
print(search(l, 15, low=0, high=len(l)-1))