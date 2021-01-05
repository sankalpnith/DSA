# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# n=3 -> ["((()))","(()())","(())()","()(())","()()()"]

def generate(n, s, left, right, answer):
    if len(s) == 2*n:
        answer.append(s)
    if left < n:
        generate(n, s+'(', left+1, right, answer)
    if right < left:
        generate(n, s + ')', left, right+1, answer)
    return answer

def generateParenthesis(n):
    if n == 1:
        return ['()']
    return generate(n, '', 0, 0, [])
    # previous_output = generateParenthesis(n-1)
    # # create two sets
    # output = set()
    # for data in previous_output:
    #     output.add("()"+data)
    #     output.add(data+'()')
    #     output.add('('+data+')')
    # return list(output)

print(generateParenthesis(4))
