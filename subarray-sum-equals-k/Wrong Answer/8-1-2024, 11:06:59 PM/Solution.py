// https://leetcode.com/problems/subarray-sum-equals-k

class Solution(object):
    def subarraySum(self, nums, k):
        pointer_1 = 0
        pointer_2 = 0
        sumation = 0
        count_array = 0

        while pointer_2 < len(nums) and pointer_1 < len(nums):
            sumation += nums[pointer_1]
            if sumation == k:
                count_array += 1
            
            elif sumation > k:
                while pointer_2 < len(nums) and sumation > k:
                    sumation = sumation - nums[pointer_2]
                    if sumation == k:
                        count_array += 1
                    pointer_2 += 1
            pointer_1 += 1
        return count_array

