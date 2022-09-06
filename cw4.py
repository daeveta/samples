# def prepare():
#     a_list = [1, 1, 2, 3, 2, 1, 1, 4, 4, 2]
#     a_dict = dict()
#     a_b = set(a_list)
#     return a_list, a_dict, a_b
#
#
# def process_list_elements(**args):
#     # print(args)
#     for el in args['a_b']:
#         # list.count(el)
#         args['a_dict'][el] = args['a_list'].count(el)
#     return args['a_dict']
#
# def process_dictionary(dictionary: int):
#     s = set()
#     for key, value in dictionary.items():
#         for el in range(1, value + 1):
#             if el == 1:
#                 s.add(str(key))
#             else:
#                 s.add(str(key) * el)
#     return s
#
# a, d, b = prepare()
# d = process_list_elements(a_list=a, a_b=b, a_dict=d)
#
# print(d)
# s = set()
# for key, value in d.items():
#     for el in range(1, value+1):
#         if el == 1:
#             s.add(str(key))
#         else:
#             s.add(str(key)*el)
# print(s)

# ln = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def is_even(test_value):
#     return test_value % 2 == 0
#
# print(list(filter(is_even, ln)))
from functools import reduce
from datetime import datetime

def stringarator(ugly_function):
    def wrapper(*args):
        t1 = datetime.now()
        r = str(ugly_function(*args))
        t2 = datetime.now()
        print(t2 - t1)
        return r
    return wrapper

@stringarator
def factorial(n):
    fctrl = 1
    for i in range(2, n+1):
        fctrl *= i
    return fctrl


n = 10
ln = list(range(1, 11))

print(type(factorial(n)))
print(factorial(n))
print(reduce(lambda rx, x: rx*x, ln))

# this is out test from other script 
print("some text")
