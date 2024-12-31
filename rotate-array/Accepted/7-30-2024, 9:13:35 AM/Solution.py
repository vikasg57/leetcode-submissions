// https://leetcode.com/problems/rotate-array

import math
class Solution(object):
    def reverse(self, array, start, end):
        while start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k , n - 1)
        self.reverse(nums, 0, n - 1)
