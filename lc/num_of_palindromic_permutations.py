from collections import Counter
def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def calculate(s):
    counter =Counter(s)
    result = fact(len(s)//2)
    odd_found = False
    for key, value in counter.items():
        if value % 2 == 1:
            if odd_found:
                return 0
            odd_found = True
        print(value)
        half = value//2
        result //= fact(half)
    return result

print(calculate("aab"))