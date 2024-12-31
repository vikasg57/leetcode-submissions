// https://leetcode.com/problems/longest-consecutive-sequence

class Solution(object):
    def longestConsecutive(self, nums):

        nums = sorted(set(nums))

        count = 1

        max_count = 0

        for i in range(len(nums) - 1):
            if nums[i]+ 1 == nums[i+1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        if max_count == 0:
            return len(nums)
        return max_count
