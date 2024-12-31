// https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):

        triple_set = set()

        for i in range(len(nums)):
            storage = set()
            for j in range(i+1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in storage:
                    triple = [nums[i], nums[j], third]
                    triple.sort()
                    triple_set.add(tuple(triple))   
                storage.add(nums[j])
        return [list(triple) for triple in triple_set]
