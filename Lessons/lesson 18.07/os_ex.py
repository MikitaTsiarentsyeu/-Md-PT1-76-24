import os

levels = ["home", "user", "new folder"]

# print('\\'.join(levels))

print(os.name)

# print(('\\' if os.name == 'nt' else '/').join(levels))

print(os.sep.join(levels))

dir = os.path.join("home", "user", "folder")

print(os.getcwd())

# os.makedirs(dir)

os.chdir(dir)

print(os.getcwd())

open("test.txt", "w")