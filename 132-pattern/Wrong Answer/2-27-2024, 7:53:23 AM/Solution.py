// https://leetcode.com/problems/132-pattern

class Solution(object):
    def find132pattern(self, nums):
        # firstly we will find ngr and nsr
        stack = []
        ngr = []
        
        for i in range(len(nums)-1, -1, -1):
            if not stack:
                ngr.append(-1)
            elif stack and stack[-1][0] > nums[i]:
                ngr.append(stack[-1][1])
            elif stack and stack[-1][0] <= nums[i]:
                while stack and stack[-1][0] <= nums[i]:
                    stack.pop()
                if stack:
                    ngr.append(stack[-1][1])
                else:
                    ngr.append(-1)
            stack.append((nums[i], i))
        ngr.reverse()

        stack = []
        nsr = []

        for i in range(len(nums)-1, -1, -1):
            if not stack:
                nsr.append(-1)
            elif stack and stack[-1][0] < nums[i]:
                nsr.append(stack[-1][1])
            elif stack and stack[-1][0] >= nums[i]:
                while stack and stack[-1][0] >= nums[i]:
                    stack.pop()
                if stack:
                    nsr.append(stack[-1][1])
                else:
                    nsr.append(-1)
            stack.append((nums[i], i))
        nsr.reverse()

        print(ngr)
        print(nsr)

        for i in range(len(nums)):
            if ngr[i] != -1:
                nxt = ngr[i] 
                if nsr[nxt] != -1:
                    if nums[i] < nums[nsr[nxt]]:
                        return True
        return False
        
