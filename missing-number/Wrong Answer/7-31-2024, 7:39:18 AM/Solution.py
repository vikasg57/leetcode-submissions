// https://leetcode.com/problems/missing-number

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        missing_number = 0
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            elif nums[0] == 1:
                return 0
        for i in range(len(nums)-1):
            if nums[i] + 1 != nums[i+1]:
                missing_number = nums[i] + 1
        if missing_number == 0:
            return len(nums)
        return missing_number
