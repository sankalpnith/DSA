# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

def nextPermutation(self, nums: List[int]) -> None:
    length = len(nums)
    if length == 1:
        return
    i = length - 1
    # find the element from right to left which is less than the next element
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i == 0:
        nums.reverse()
    else:
        j = length - 1
        # find the first element from the end which is greater than nums[i] and swap them and then sort(reverse) the end part
        while j > 0 and nums[j] <= nums[i - 1]:
            j -= 1
        nums[j], nums[i - 1] = nums[i - 1], nums[j]

        nums[i:] = nums[-1:i - 1:-1]
