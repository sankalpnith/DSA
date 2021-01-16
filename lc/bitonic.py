#You are given an integer array nums sorted in ascending order, and an integer target.
#Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#If target is found in the array return its index, otherwise, return -1.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bitonic_index = self.find_bitonic(nums)
        low, high = 0, len(nums) - 1
        print(bitonic_index)
        if nums[bitonic_index] == target:
            return bitonic_index
        result = self.bin_search(nums, low, bitonic_index - 1, target)
        if result == -1:
            result = self.bin_search(nums, bitonic_index + 1, high, target)
        return result

    def find_bitonic(self, nums):
        low, high = 0, len(nums) - 1
        ele_to_compare = nums[-1]
        while low < high:
            mid = low + (high - low) // 2
            if ele_to_compare >= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def bin_search(self, nums, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
