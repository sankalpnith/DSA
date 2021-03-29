#Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
class Solution:
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]
        ans,cur_max,cur_min = -sys.maxsize,0,0
        for num in nums:
            if num>=0:
                cur_max,cur_min = max(num,num*cur_max), min(num,num*cur_min)
            else:
                cur_max,cur_min = max(num,num*cur_min), min(num,num*cur_max)
            ans = max(ans,cur_max)
        return ans
