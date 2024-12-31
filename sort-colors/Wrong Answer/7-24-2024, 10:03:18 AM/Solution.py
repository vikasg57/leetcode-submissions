// https://leetcode.com/problems/sort-colors

class Solution(object):
    def sortColors(self, nums):
        left_pointer= 0
        right_pointer = len(nums) - 1
        iterate_pointer = 0

        while iterate_pointer <= right_pointer:
            if nums[iterate_pointer] == 0:
                nums[left_pointer], nums[iterate_pointer]=nums[iterate_pointer], nums[left_pointer]
                left_pointer += 1
                iterate_pointer += 1
            elif nums[iterate_pointer] == 2:
                nums[right_pointer], nums[iterate_pointer]=nums[iterate_pointer], nums[right_pointer]
                right_pointer -= 1
                iterate_pointer += 1
            else:
                iterate_pointer += 1
