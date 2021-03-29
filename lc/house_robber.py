# https://leetcode.com/problems/house-robber/
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

def rob(self, nums: List[int]) -> int:
    robbed = 0
    n = len(nums)
    if n == 0:
        robbed = 0
    elif n == 1:
        robbed = nums[0]
    elif n == 2:
        robbed = max(nums[0], nums[1])
    else:
        rob = [None] * len(nums)
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            rob[i] = max(nums[i] + rob[i - 2], rob[i - 1])
        robbed = rob[-1]
    return robbed

# https://leetcode.com/problems/house-robber-ii/

# same problem as above but the houses are connected in a circle
# ides is to find max between two arrays like nums[1:], nums[:-1

class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            robbed = 0
        elif n == 1:
            robbed = nums[0]
        elif n == 2:
            robbed = max(nums[0], nums[1])
        else:
            robbed = max(self.simple_rob(nums[:-1]), self.simple_rob(nums[1:]))
        return robbed

    def simple_rob(self, nums):
        rob = [None] * len(nums)
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            rob[i] = max(nums[i] + rob[i - 2], rob[i - 1])
        return rob[-1]
