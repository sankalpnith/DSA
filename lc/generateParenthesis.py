# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# n=3 -> ["((()))","(()())","(())()","()(())","()()()"]
# similar to print all permutations
def generate(n, s, left, right, answer):
    if len(s) == 2*n:
        answer.append(s)
    if left < n:
        generate(n, s+'(', left+1, right, answer)
    if right < left:
        generate(n, s + ')', left, right+1, answer)
    return answer


def generateParenthesis(n):
    return generate(n, '', 0, 0, [])


print(generateParenthesis(1))
