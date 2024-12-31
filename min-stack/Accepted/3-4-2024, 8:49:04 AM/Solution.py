// https://leetcode.com/problems/min-stack

class MinStack(object):

    def __init__(self):
        self.min_ele = -1
        self.stack = []
        

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min_ele = val
        else:
            if val >= self.min_ele:
                self.stack.append(val)
            elif val < self.min_ele:
                self.stack.append(val * 2 - self.min_ele)
                self.min_ele = val

    def pop(self):
        if not self.stack:
            return -1
        else:
            if self.stack and self.stack[-1] >= self.min_ele:
                self.stack.pop()
            elif self.stack and self.stack[-1] < self.min_ele:
                self.min_ele = 2 * self.min_ele - self.stack[-1]
                self.stack.pop()

    def top(self):
        if not self.stack:
            return -1
        else:
            if self.stack and self.stack[-1] >= self.min_ele:
                return self.stack[-1]
            elif self.stack and self.stack[-1] < self.min_ele:
                return self.min_ele
        

    def getMin(self):
        if not self.stack:
            return -1
        return self.min_ele


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()