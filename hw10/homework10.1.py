symbols = "0123456789 -+/*"
while True:
    x = "x ="
    y = input("Enter your expression: ")
    x += y
    if False in [a in symbols for a in y]:
        print("Failed. Try again!")
        continue
    exec(x)
    print(x)


