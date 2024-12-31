// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j, num_2 in enumerate(nums):
                if i != j:
                    add = num + num_2
                    if add == target:
                        return (i, j)

            
