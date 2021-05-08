# https://leetcode.com/problems/min-stack/submissions/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # [(val, min_value)]
        self.stack=[]

    def push(self, val: int) -> None:
        if self.stack:
            if val < self.stack[-1][1]:
                self.stack.append((val,val))
            else:
                self.stack.append((val,self.stack[-1][1]))
        else:
            self.stack.append((val,val))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()