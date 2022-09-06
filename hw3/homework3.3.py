# def set_gen(list):
#     i = 0
#     while i < len(list):
#         count = list.count(list[i])
#         if count > 1:
#             list[index] = str(list[i) * count
#         index += 1
#
#     return set(list)
# list = [5, 5, 6, 7, 4, 5]
# print(set_gen(list))

list = [1, 1, 2, 3, 2, 1, 1, 4, 4, 2]
# list = input('enter a list of numbers separated with space: ').split()

d = dict()
a = set(list)
for el in a:
    # list.count(el)
    d[el] = list.count(el)
s = set()
for key, value in d.items():
    for el in range(1, value+1):
        if el == 1:
            s.add(str(key))
        else:
            s.add(str(key)*el)
print(s)
print(len(list) == len(s))