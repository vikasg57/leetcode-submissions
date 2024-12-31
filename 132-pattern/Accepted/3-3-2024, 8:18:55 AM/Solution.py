// https://leetcode.com/problems/132-pattern

class Solution(object):
    def find132pattern(self, nums):

        if len(nums) < 3:
            return False
        lme = [0] * len(nums)
        lme[0] = nums[0]

        for i in range (1, len(nums)):
            if nums[i] < lme[i-1]:
                lme[i] = nums[i]
            else:
                lme[i] = lme[i-1]
        
        stack = []
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > lme[i]:
                while stack and stack[-1] <= lme[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False
