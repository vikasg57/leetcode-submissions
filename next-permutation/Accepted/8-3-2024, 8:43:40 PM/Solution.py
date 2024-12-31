// https://leetcode.com/problems/next-permutation

class Solution(object):
    def nextPermutation(self, nums):
        break_point = -1
        for i in range(len(nums) -2 , -1, -1):
            if nums[i] < nums[i+1]:
                break_point = i
                break
        if break_point == -1:
            return nums.reverse()
        for i in range(len(nums) -1, 0, -1):
            if nums[i] > nums[break_point]:
                nums[i], nums[break_point] = nums[break_point], nums[i]
                break
        self.reverse(nums, break_point + 1, len(nums) -1)
        return nums
        
    def reverse(self, array, start, end):
        while start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
