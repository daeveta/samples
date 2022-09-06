# def result_count(num, data):
#     count = 0
#     for el in data:
#         if el == num:
#             count += 1
#     return count


number = [1, 1, 4, 2, 4, 4]
result_dict = {}
for num in number:
    if num not in result_dict:
        result_dict[num] = (lambda n, ln: sum([1 for i in ln if n == i]))(num, number)

print(result_dict)
