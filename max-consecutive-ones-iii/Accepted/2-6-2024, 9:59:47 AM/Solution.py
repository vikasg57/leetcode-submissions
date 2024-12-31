// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution(object):
    def longestOnes(self, nums, k):

        left = 0

        count = 0
        max_count = 0

        left = 0

        for i in range(0, len(nums)):
            if nums[i] ==0:
                count += 1
            
            while count > k:
                if nums[left] == 0: 
                    count -= 1
                left += 1
            max_count = max(max_count, i - left + 1)

        return max_count
