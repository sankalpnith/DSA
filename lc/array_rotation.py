def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    self.reverse(nums, 0, n - 1)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, n - 1)


def reverse(self, nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# this logic will work both for rotate left and rotate right

# Start with the logic below

def left_rotate_by_one(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1] # Left
        # shift by one
    arr[n - 1] = temp


def leftRotate(arr, d, n):
    for i in range(d):
        left_rotate_by_one(arr, n)


def right_rotate_by_one(arr, n):
    temp = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1] # Right
        # shift by one
    arr[0] = temp


def rightRotate(arr, d, n):
    for i in range(0, d):
        right_rotate_by_one(arr, n)
