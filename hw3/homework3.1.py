x = 0
b = False
while (b == False):
    name = input('Введите свое имя: ')
    for a in name:
        if (a.isalpha() is True):
            b = True
        else:
            b = False
            x += 1
            break

c = False
while (c == False):
    age = input('Сколько Вам лет?')
    for a in age:
        if (a.isdigit() is True) or (age[0] == '-'):
            c = True
        else:
            c = False
            x += 1
            break

else:
    int_age = int(age)


if int_age < 0:
    int_age = int(input('Сколько Вам лет?'))
    if (int_age < 0) or (int_age > 100):
        print(f'{name}, так не бывает!')
    else:
        print(f'Cool')
elif int_age < 3:
    print(f'{name}, ты слишком молодо выглядишь!')
elif int_age < 10:
    print(f'Привет, шкет {name}')
elif int_age < 18:
    print(f'Как жизнь, {name}?')
elif int_age < 100:
    print(f'Чего желаете, {name}?')
else:
    int_age = int(input('Сколько Вам лет?'))
    if (int_age < 0) or (int_age > 100):
        print(f'{name}, у нас столько не живут')
    else:
        print(f'Молодец')

if x == 0:
    print('Молодец, сделал с первого раза!')
else:
    print('Вот так бы сразу!')