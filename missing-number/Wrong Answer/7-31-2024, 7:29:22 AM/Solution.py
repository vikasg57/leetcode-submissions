// https://leetcode.com/problems/missing-number

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        missing_number = 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                pass
            else:
                missing_number = nums[i] + 1
        if missing_number == 0:
            return len(nums)
        return missing_number
