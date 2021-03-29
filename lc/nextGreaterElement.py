#https://leetcode.com/problems/next-greater-element-i/submissions/

def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    output = [-1] * len(nums2)
    stack = []
    for index in range(len(nums2)):
        while stack and nums2[index] > nums2[stack[-1]]:
            output[stack.pop()] = nums2[index]
        stack.append(index)
    print(output)
    result = []
    for num in nums1:
        result.append(output[nums2.index(num)])
    return result


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    mapping = {}
    for num in nums2:
        while stack and num > stack[-1]:
            mapping[stack[-1]] = num
            stack.pop()
        stack.append(num)
    for data in stack:
        mapping[data] = -1
    result = []
    for num in nums1:
        result.append(mapping[num])
    return result

# https://leetcode.com/problems/next-greater-element-ii/submissions/
# next greater element circular array
def nextGreaterElements(self, nums: List[int]) -> List[int]:
    size = len(nums)
    loop_count = 2* len(nums)
    stack =[]
    result = [-1]*size
    for i in range(loop_count):
        i %= size
        while stack and nums[i] > nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result