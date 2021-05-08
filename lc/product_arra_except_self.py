# https://leetcode.com/problems/product-of-array-except-self/submissions/

def productExceptSelf(self, nums: List[int]) -> List[int]:
    product = [1 for _ in nums]

    temp = 1
    for i in range(len(nums)):
        product[i] *= temp
        temp *= nums[i]
    temp = 1
    for i in range(len(nums) - 1, -1, -1):
        product[i] *= temp
        temp *= nums[i]

    return product