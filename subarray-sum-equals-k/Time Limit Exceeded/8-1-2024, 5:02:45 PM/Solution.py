// https://leetcode.com/problems/subarray-sum-equals-k

class Solution(object):
    def subarraySum(self, nums, k):
        array_count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    array_count += 1
        return array_count