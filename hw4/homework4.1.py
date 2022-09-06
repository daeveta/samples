dict_orig = {1: 'key', 2: 'value', 3: 'number', 4: 'word'}
def dictionary(dict1):
    dict2 = {}
    for i in dict1:
        dict2[dict1.get(i)] = i
    return dict2

print(dictionary(dict_orig))


