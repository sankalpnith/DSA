# https://leetcode.com/problems/fraction-to-recurring-decimal/

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
#
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# Example 4:
#
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
# Example 5:
#
# Input: numerator = 1, denominator = 5
# Output: "0.2"


def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    print(str(numerator / denominator))
    if numerator == 0:
        return "0"
    result = []
    if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
        result.append('-')
    numerator, denominator = abs(numerator), abs(denominator)
    result.append(str(numerator // denominator))
    remainder = numerator % denominator
    if remainder == 0:
        return ''.join(result)
    result.append('.')
    d = {}
    while remainder != 0:
        if remainder in d:
            result.insert(d[remainder], '(')
            result.append(')')
            break
        d[remainder] = len(result)

        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator
    return ''.join(result)
