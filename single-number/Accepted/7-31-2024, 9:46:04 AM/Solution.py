// https://leetcode.com/problems/single-number

class Solution(object):
    def singleNumber(self, nums):
        obj = {}
        for i in range(len(nums)):
            if nums[i] in obj:
                obj[nums[i]] =  obj[nums[i]] + 1
            else:
                 obj[nums[i]] = 1
        for tup in obj.items():
            if tup[1] == 1:
                return tup[0]

