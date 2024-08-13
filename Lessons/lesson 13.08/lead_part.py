dependent_part = "some value"
import dependent_part as dp
# from dependent_part import test as dp_test
# from dependent_part import *
# import math
# import csv
from dir import test


print(test)

print(dependent_part)
print(dp.test)
print(dp)

print(__name__)
print(dp.__name__)

# print(math.pi)

# print(csv.QUOTE_NONE)

if __name__ == "__main__":
    pass


