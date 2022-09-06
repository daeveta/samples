list1 = ('топот', 'кек', 'лес')
list1 = list(filter(lambda x: x == str(''.join(reversed(x))), list(list1)))
print(list1)