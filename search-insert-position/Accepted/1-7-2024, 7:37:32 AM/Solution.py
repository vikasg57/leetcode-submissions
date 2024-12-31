// https://leetcode.com/problems/search-insert-position

class Solution(object):
    def searchInsert(self, nums, target):
        
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            if target > nums[len(nums)-1]:
                return len(nums)
            if target < nums[0]:
                return 0
            if (i <= len(nums) -  2
             and target > nums[i]
             and target < nums[i+1]):
                return i+1
