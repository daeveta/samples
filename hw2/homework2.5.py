number = '1234561233'
# a = set(number)
count = []
for a in number:
    count.append((number.count(a), int(a)))
list_count = list(set(count))
list_count.sort(reverse=True)

for (x, y) in list_count[0:3]:
    print(f' Количество {x} чисел {y}')



