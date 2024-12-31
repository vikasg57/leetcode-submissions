// https://leetcode.com/problems/single-number

class Solution(object):
    def singleNumber(self, nums):
        
        duplicate_dict = {}
        
        for i in range(0, len(nums)):
            duplicate_dict[nums[i]]= duplicate_dict.get(nums[i], 0) + 1
        ans = 0
        for key, val in duplicate_dict.items():
            if val == 1:
                ans = key
        return ans
                