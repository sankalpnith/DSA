#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/submissions/
#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/
# replace k with 2 if remove duplicates only
def removeDuplicates(self, s: str, k: int) -> str:
    stack = []
    for char in s:
        if stack and stack[-1][0] == char:
            if stack[-1][1] == k - 1:
                stack.pop()
            else:
                stack[-1][1] += 1
        else:
            stack.append([char, 1])
    result = []
    for c, n in stack:
        result.append(c * n)
    return "".join(result)

# Similar to above but remove all duplicates
def removeConsecutiveCharacter(self, S):
    # code here
    stack = []
    for char in S:
        if stack:
            if stack[-1][0] != char:
                if stack[-1][1] > 1:
                    stack.pop()
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
        else:
            stack.append([char,1])
    if stack[-1][1] > 1:
        stack.pop()
    result =[]
    for c,n in stack:
        result.append(c*n)
    return "".join(result)
