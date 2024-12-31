// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

class Solution(object):
    def check(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)% len(nums)] :
                count += 1
        if count > 1:
            return False
        return True