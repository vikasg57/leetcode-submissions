// https://leetcode.com/problems/rotate-array

import math
class Solution(object):
    
    def rotate(self, nums, k):
        if k > 0 :
            for i in range(0, len(nums)):
                temp = nums[len(nums)-1]
                nums.pop()
                nums.insert(0, temp)
                if k > len(nums):
                    k = k % len(nums)
                if i == k-1:
                    break                