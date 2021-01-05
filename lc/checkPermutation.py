from collections import defaultdict


def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    dict_str1 = defaultdict(int)
    dict_str2 = defaultdict(int)

    for char in str1:
        dict_str1[char] += 1
    for char in str2:
        dict_str2[char] += 1
    for key, value in dict_str1.items():
        if dict_str2[key] != value:
            return False
    return True


str1 = 'b'
str2 = 'd'
print(checkPermutation(str1, str2))

