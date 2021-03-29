# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent. Return the answer in any order

def combination(digits):
    mapping = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
    }
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(mapping[digits[-1]])
    previous = combination(digits[:-1])
    additional = list(mapping[digits[-1]])
    return [s+c for s in previous for c in additional]
    # return [s+c for s in additional for c in previous]
output = combination('234')
print(output)