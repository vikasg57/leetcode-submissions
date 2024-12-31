// https://leetcode.com/problems/max-consecutive-ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        one_count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                one_count += 1
            else:
                one_count = 0
            max_count = max(max_count, one_count)
        return max_count        
