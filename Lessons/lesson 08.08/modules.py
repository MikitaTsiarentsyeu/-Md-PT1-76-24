"this is my module"

import math

print(math.__dict__["pi"])
print(math.pi)

import my_module

print(my_module, type(my_module))

print(my_module.__dict__)

print(my_module.test_val)

my_module.test_func()