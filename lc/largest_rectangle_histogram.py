# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, height) -> int:
        # create a strictly increasing monotonic stack
        height.append(0)
        stack = [-1]
        area=0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] -1
                area = max(area, h*w)
            stack.append(i)
        return area
