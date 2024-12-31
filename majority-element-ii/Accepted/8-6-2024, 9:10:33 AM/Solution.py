// https://leetcode.com/problems/majority-element-ii

class Solution(object):
    def majorityElement(self, nums):

        obj = {}
        vector = []

        for i in range(len(nums)):

            if nums[i] in obj:
                obj[nums[i]] +=  1
            else:
                obj[nums[i]] =  1
        
        limit = len(nums) / 3
        
        for obj in obj.items():
            if obj[1] > limit:
                vector.append(obj[0])
        return vector