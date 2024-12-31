// https://leetcode.com/problems/132-pattern

class Solution(object):
    def find132pattern(self, nums):
        min_i = float('inf')
        for j in range(len(nums) - 1):
            min_i = min(min_i, nums[j])
            for k in range(j + 1, len(nums)):
                if min_i < nums[k] < nums[j]:
                    return True
        return False
        
