# https://leetcode.com/problems/permutations/
#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# similar to generate parenthesis
def permute(nums):
    result = []
    create(nums, [], result)
    print(result)


def create(nums, path, result):
    if not nums:
        result.append(path)
    for i in range(len(nums)):
        create(nums[:i] + nums[i + 1:], path + [nums[i]], result)


permute([1,2,3])