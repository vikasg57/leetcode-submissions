// https://leetcode.com/problems/maximum-subarray

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        quick_sum = 0
        for i in range(len(nums)):
            quick_sum += nums[i]

            if quick_sum > max_sum:
                max_sum = quick_sum
            if quick_sum < 0:
                quick_sum = 0

        return max_sum