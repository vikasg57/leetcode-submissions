// https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution(object):
    def maxOperations(self, nums, k):
        result = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                num = k - nums[i]
                for j in range(i+1, len(nums)):
                    if nums[j]!=0 and nums[j] == num:
                        result += 1
                        nums[j] = 0
                        nums[i] = 0
                        break
        return result
