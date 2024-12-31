// https://leetcode.com/problems/move-zeroes

class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                while j < len(nums) - 1:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    j += 1
