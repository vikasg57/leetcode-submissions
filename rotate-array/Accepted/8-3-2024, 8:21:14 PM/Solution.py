// https://leetcode.com/problems/rotate-array

import math
class Solution(object):
    
    def rotate(self, nums, k): 
        n = len(nums)
        k = k % n
        temp_array = []

        for i in range(n - k):
            temp_array.append(nums[i])

        index = 0
        for i in range(n - k, n):
            nums[index] = nums[i]
            index += 1

        index = 0
        for i in range(k, n):
            nums[i] = temp_array[index]
            index += 1
