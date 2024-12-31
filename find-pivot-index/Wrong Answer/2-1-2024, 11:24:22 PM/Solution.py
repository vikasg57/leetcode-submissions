// https://leetcode.com/problems/find-pivot-index

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        add = 0
        for i in range(0, len(nums)):
            add += nums[i]
        add_2 = add
        result = -1
        for i in range(0, len(nums)):
            add_2 -= nums[i]
            if add_2 == (add-nums[i])/2:
                result = i
        return result
