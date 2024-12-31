// https://leetcode.com/problems/maximum-subarray

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        for i in range(len(nums)):
            addition = 0
            for j in range(i, len(nums)):
                addition += nums[j]
                if addition > max_sum:
                    max_sum = addition
        return max_sum