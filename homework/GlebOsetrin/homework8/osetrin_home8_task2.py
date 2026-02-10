def fibonaci(limit=1000000):
    a = 1
    b = 1
    count = 1

    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


count = 1


for number in fibonaci(100000000):
    if count == 5:
        print('пятое', number)
    if count == 200:
        print('двухсотое', number)
    if count == 1000:
        print('тысячное', number)
    if count == 100000:
        print('стотысячное', number)
        break
    count += 1
