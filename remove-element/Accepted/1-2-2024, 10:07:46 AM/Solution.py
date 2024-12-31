// https://leetcode.com/problems/remove-element

class Solution(object):
    def removeElement(self, nums, val):

        ind = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1
        return ind
        