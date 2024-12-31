// https://leetcode.com/problems/majority-element

class Solution(object):
    def majorityElement(self, nums):

        obj = {}
        majority = 0
        majority_ele = 0

        for i in range(len(nums)):
            if nums[i] in obj:
                obj[nums[i]] += 1
                majority = max(obj[nums[i]], majority)
                if majority == obj[nums[i]]:
                    majority_ele = nums[i]
            else:
                obj[nums[i]] = 1
        
        return majority_ele
        