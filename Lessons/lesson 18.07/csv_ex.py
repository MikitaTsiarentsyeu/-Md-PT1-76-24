# with open("test.csv", 'r') as f:
#     skip = True
#     for line in f:
#         if skip:
#             skip = False
#             continue
#         print(line.split(',')[0])


snieker = ["adidas", 5646546, "red", "court"]

# with open("test.csv", 'a') as f:
#     f.write(f"\n{','.join([str(x) for x in snieker])}")


import csv

with open("test.csv", 'r') as f:
    reader = csv.reader(f)
    for record in reader:
        print(record)

with open("test.csv", 'a', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(snieker)
    writer.writerow(snieker)

with open("test.csv", 'r') as f:
    reader = csv.DictReader(f)
    for record in reader:
        print(record)

with open("test.csv", 'a', newline='\n') as f:
    writer = csv.DictWriter(f, ['brand', "sku", "color", "model"])
    writer.writerow({'brand': 'nike', 'sku': '', 'color': 'white', 'model': 'air'})