# https://leetcode.com/problems/largest-number/submissions/
# Input: nums = [10,2]
# Output: "210"
# Example 2:
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

from functools import cmp_to_key # used to pass function that expects two args

class Solution:

    def largestNumber(self, nums):

        def compare(x, y):
            if int(x + y) > int(y + x):
                return -1
            else:
                return 1

        numstr = list(map(str, nums))
        a = sorted(numstr, key=cmp_to_key(compare))
        return a[0] if a[0] == '0' else "".join(a)