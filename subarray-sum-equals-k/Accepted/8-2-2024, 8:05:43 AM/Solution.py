// https://leetcode.com/problems/subarray-sum-equals-k

class Solution(object):
    def subarraySum(self, nums, k):

        prefix_sum = {0:1}
        sumation = 0
        count = 0

        for i in range(len(nums)):
            sumation += nums[i]
            if sumation-k in prefix_sum:
                count += prefix_sum[sumation-k]
            if sumation in prefix_sum:
                prefix_sum[sumation] += 1
            else:
                prefix_sum[sumation] = 1
        
        return count
