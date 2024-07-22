
# with open("photo.jpg", "rb") as f:
#     # print(f.read())
#     print(f.read(10))


# with open("test_bin.txt", "wb") as f:
#     f.write(b"some binary string")
#     f.write(b'\xff\xd8\xff\xe1czExif')

import time



chunk_size = 1

start = time.time()
count = 0

with open("test.pdf", "rb") as donor:
    with open("test copy.pdf", "wb") as recepient:
        chunk = True
        while chunk:
            chunk = donor.read(chunk_size)
            recepient.write(chunk)
            count += 1

finish = time.time()

print(finish - start, count)