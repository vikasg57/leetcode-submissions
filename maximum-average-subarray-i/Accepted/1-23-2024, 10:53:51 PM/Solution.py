// https://leetcode.com/problems/maximum-average-subarray-i

class Solution(object):
    def findMaxAverage(self, nums, k):
        sum_int = 0
        max_value = float("-inf")
        for i in range(0, len(nums)):
            if i < k:
                sum_int += nums[i]
            if i >= k and sum_int > max_value:
                max_value = sum_int
            if i >= k:
                sum_int += nums[i]
                sum_int -= nums[i - k]
            if i >= k and sum_int > max_value:
                max_value = sum_int
        if len(nums) == k:
            max_value = sum_int
            avg_int = float(max_value)/float(k)
        else:
            avg_int = float(max_value)/float(k)
        avg_int = float(format(avg_int, '.5f'))
        return avg_int