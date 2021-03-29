#Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sub_array =[None]*n
        max_sub_array[0] = nums[0]
        for i in range(1,n):
            max_sub_array[i] = max(nums[i]+max_sub_array[i-1], nums[i])
        return max(max_sub_array)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum,ans = 0,nums[0]
        for num in nums:
            sum = max(num +sum, num)
            ans = max(ans, sum)
        return ans
