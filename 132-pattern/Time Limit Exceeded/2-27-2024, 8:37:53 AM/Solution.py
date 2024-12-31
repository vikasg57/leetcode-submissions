// https://leetcode.com/problems/132-pattern

class Solution(object):
    def find132pattern(self, nums):
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False

        
