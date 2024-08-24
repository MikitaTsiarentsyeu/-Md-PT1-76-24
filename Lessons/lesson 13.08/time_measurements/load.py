import measure

def test(n):
    for i in range(n):
        i+=1

measure.start()
test(100000)
print(measure.finish())
