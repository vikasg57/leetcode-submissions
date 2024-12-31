// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums

class Solution(object):
    def rangeSum(self, nums, n, left, right):
        subarray_sum = []
        ans = 0
        for i in range(len(nums)):
            sumation = 0
            for j in range(i, len(nums)):
                sumation += nums[j]
                subarray_sum.append(sumation)
        subarray_sum.sort()
        print(subarray_sum)
        print(left, right)
        print(len(subarray_sum))
        for i in range(left, right + 1):
            ans += subarray_sum[i-1]
        return ans 