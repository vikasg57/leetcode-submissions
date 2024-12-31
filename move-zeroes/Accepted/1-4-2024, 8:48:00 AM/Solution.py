// https://leetcode.com/problems/move-zeroes

class Solution(object):
    def moveZeroes(self, nums):
        
        index_2 = len(nums) - 1
        
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for i in range(0, len(nums)):
            if i >= index:
                nums[i] = 0
        return nums
            