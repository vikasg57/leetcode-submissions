// https://leetcode.com/problems/rotate-array

import math
class Solution(object):
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if k > 0 :
            for i in range(0, len(nums)):
                temp = nums[len(nums)-1]
                nums.pop()
                nums.insert(0, temp)
                if k > len(nums):
                    k = k % len(nums)
                    print(k)
                if i == k-1:
                    break
            
        