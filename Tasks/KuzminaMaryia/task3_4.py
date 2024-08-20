num = input("Enter numbers separated by spaces: ")
numb = list(map(int, num.split()))
numb.sort()
max2 = numb.pop(-2)
   
print("Second largest number: ", max2)