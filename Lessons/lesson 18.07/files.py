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


with open("test.txt", 'a+') as f:
    print(repr(f.read()))
    f.write("test line from a+\n")
    f.seek(0)
    print(repr(f.read(10)))
    f.write("another line from a+\n")


with open("test.txt", 'r+') as f:
    print(repr(f.read()))
    f.write("test line from r+\n")
    print(repr(f.read()))
    f.seek(0)
    f.write("another line from r+\n")
    print(repr(f.read()))

with open("test.txt", 'w+') as f:
    print(repr(f.read()))
    f.write("new content")
    f.seek(0)
    print(repr(f.read(2)))
    f.write("test")