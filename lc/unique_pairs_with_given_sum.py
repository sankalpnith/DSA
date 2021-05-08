

def calculate(nums, target):
    visited = set()
    ans = set()
    for num in nums:
        if target - num in visited:
            pair = (num, target-num) if num > target-num else (target-num, num)
            if pair not in ans:
                ans.add(pair)
        visited.add(num)
    return ans

nums = [5, 6, 5, 7, 7, 8]
target = 13

print(calculate(nums, target))