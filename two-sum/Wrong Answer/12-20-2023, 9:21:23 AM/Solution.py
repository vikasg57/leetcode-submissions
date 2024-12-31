// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):

        left = 0
        right = len(nums) - 1

        half_length = len(nums) / 2

        increment = 0

        while increment < half_length + 1:
            print(increment)
            print(left, right)
            add = nums[left] + nums[right]
            print(add)
            if add == target:
                return left, right
            elif add > target:
                right -= 1
            elif add < target:
                left += 1
            increment += 1
