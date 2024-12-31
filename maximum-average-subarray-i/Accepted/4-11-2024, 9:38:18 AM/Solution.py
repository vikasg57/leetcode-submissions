// https://leetcode.com/problems/maximum-average-subarray-i

class Solution(object):
    def findMaxAverage(self, nums, k):
        i = 0
        j = 0
        subarray_sum = 0
        max_sum = float('-inf')
        while j < len(nums):
            subarray_sum += nums[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                max_sum = max(subarray_sum, max_sum)
                subarray_sum -= nums[i]
                j += 1
                i += 1
        avg_int = float(max_sum)/float(k)
        avg_int = float(format(avg_int, '.5f'))
        return avg_int
