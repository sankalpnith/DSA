# Given a string. Find if it is a permutation of a palindrome
# for palindrome character count or every character is even or atmost one odd

from collections import Counter


def permutation_palindrome(str1):
    count_dict = Counter(str1)
    odd_count = 0
    for key, value in count_dict.items():
        if value % 2 == 1:
            odd_count += 1
    return odd_count <= 1


str1 = "tacatc"
print(permutation_palindrome(str1))
