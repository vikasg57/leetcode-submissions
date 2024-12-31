// https://leetcode.com/problems/max-consecutive-ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        count_one = 0
        count_max = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                count_one += 1
            else:
                count_one = 0
            count_max = max(count_max, count_one)
        return count_max
