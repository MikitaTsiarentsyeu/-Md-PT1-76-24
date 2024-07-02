s1 = "some string"
print(s1, type(s1))

s2 = 'some string'
print(s2, type(s2))

print(s1 == s2)

s = 'the street name is "Baker"'

s = "the street name is \"Baker\""

print(len("test"), len(" "), len(""), len("\n"), len("\""), len('"'))

print("\"" == '"')

s3 = '''some string'''
s4 = """some string"""

print(s1 == s2 == s3 == s4)

test_str = """line 1
line 2
line 3"""

print(test_str)

# some comment about the functionality of the program

"""some comment
about functionality
of the program"""

print(ord("A"), ord("А"), ord("a"))
print(chr(22), chr(222), chr(2222), chr(22222), chr(222222))

print(ord("👍"), chr(128077))
print(chr(128078), chr(128079), chr(128080))

x = "test "+"another test"
print(x, type(x))

greet = "hello, "
usr = input("Enter your name please:")
print(greet+usr)
print(f"hello, {usr}")


print("test"*8)