// https://leetcode.com/problems/increasing-triplet-subsequence

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        pointer_1 = 0
        pointer_2 = 0

        for i in range(0, len(nums)):
            pointer_1 = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > pointer_1:
                    pointer_2 = nums[j]
                    for k in range(j+1, len(nums)):
                        if nums[k] > pointer_2:
                            return True
        return False
                    

        