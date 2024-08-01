# download_count = 0
# clicks_count = 0
# email_count = 0


# d = {}

# def counter(name, n=0):
#     if name in d:
#         d[name] = d[name]+1
#     else:
#         d[name] = n

#     return d[name]

# print(counter("download"))
# print(counter("download"))
# print(counter("download"))

# print(counter("click"))
# print(counter("click"))

# print(counter("download"))

# d["click"] = 100

# print(counter("click"))


def counter_base(n=0):
    def inner():
        nonlocal n
        n += 1
        return n
    return inner

download_counter = counter_base()
clicks_counter = counter_base(100)

for i in range(5):
    print(download_counter())
    print(clicks_counter())