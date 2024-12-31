// https://leetcode.com/problems/longest-consecutive-sequence

class Solution(object):
    def longestConsecutive(self, nums):

        nums.sort()

        count = 1

        max_count = float('-inf')

        for i in range(len(nums) - 1):
            if nums[i]+ 1 == nums[i+1]:
                count += 1
            max_count = max(max_count, count)
        return max_count



        