// https://leetcode.com/problems/increasing-triplet-subsequence

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        pointer_1 = float('inf')
        pointer_2 = float('inf')

        for i in range(0, len(nums)):
            if nums[i] <= pointer_1:
                pointer_1 = nums[i]
            if nums[i] > pointer_1 and nums[i] <= pointer_2:
                pointer_2 = nums[i]
            if nums[i] > pointer_1 and nums[i] > pointer_2:
                return True
        return False
        