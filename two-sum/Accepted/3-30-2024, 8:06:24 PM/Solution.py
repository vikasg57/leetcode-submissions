// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        obj = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in obj:
                return [obj[diff], i]
            obj[nums[i]] = i