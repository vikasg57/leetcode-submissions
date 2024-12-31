// https://leetcode.com/problems/missing-number

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        missing_number = -1
        for i in range(len(nums)):
            if nums[0] != 0:
                missing_number = 0
            if i < len(nums) - 1 and nums[i] + 1 != nums[i+1]:
                missing_number = nums[i] + 1
        if missing_number == -1:
            return len(nums)
        return missing_number
