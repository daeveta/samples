def geometry(number, step):
    n = 1
    i = 0
    while i < number:
        if i == 0:
            yield n
        else:
            n = n * step
            yield n
        i += 1

for y in geometry(5, 3):
    print(y)


import re

email = input('Enter: ')

symbols = re.compile('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def valid(email):
    if re.fullmatch(symbols, email):
        print("valid email")
    else:
        print("invalid email")


valid(email)
