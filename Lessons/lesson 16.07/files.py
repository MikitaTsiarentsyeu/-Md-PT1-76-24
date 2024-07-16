# f = open("test.txt", 'w')

# print(f, type(f))

# f.close()

with open("test.txt", 'w') as f:
    f.write("new test content\n")
    f.writelines(["line 1\n", "line 2\n", "line 3\n"])
    f.seek(0)
    f.write("write from the start")
    # f.read() error

with open("test.txt", 'r') as f:
    # print(repr(f.read()))

    # print(repr(f.read(5)))
    # print(repr(f.read(5)))
    # print(repr(f.read(5)))
    # f.seek(0)
    # print(repr(f.read(555)))

    # lines = f.readlines()
    # print(lines)

    for line in f:
        print(repr(line))


with open("test.txt", 'a') as f:
    f.write("appended text\n")
    f.seek(0)
    f.write("prepended text\n")