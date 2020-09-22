#Given an unsorted array of integers, find the length of longest increasing subsequence.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]> nums[j] and lis[i]< lis[j] +1:
                    lis[i] = lis[j] + 1
        return max(lis) if lis else 0
