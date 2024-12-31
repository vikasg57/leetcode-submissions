// https://leetcode.com/problems/majority-element

class Solution(object):
    def majorityElement(self, nums):

        frequency = {}

        max_occurance = float('-inf')
        max_key = 0

        for i in range(0, len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1
        for k, v in frequency.items():
            if v > len(nums)/2:
                max_occurance = v
                max_key = k
                if v > max_occurance:
                    max_occurance = v
                    max_key = k
        return max_key