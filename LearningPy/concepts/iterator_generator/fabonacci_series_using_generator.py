def fabonacci_series(count):
    counter = 0
    a = 0
    b = 1
    while True:
        if counter == count:
            break
        yield a
        counter += 1
        a, b = b, a + b


# usual way
for x in fabonacci_series(10):
    print(x)

# simplified
print(list(fabonacci_series(5)))