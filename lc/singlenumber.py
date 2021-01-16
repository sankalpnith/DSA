# Given an integer array nums where every element appears three times except for one,
# which appears exactly once. Find the single element and return it.

# Input: nums = [2,2,3,2]
# Output: 3

def singleNumber(nums):
    ones, twos = 0, 0
    for num in nums:
        twos |= ones & num
        ones ^= num
        not_threes = ~(ones & twos)
        ones &= not_threes
        twos &= not_threes
    return ones
