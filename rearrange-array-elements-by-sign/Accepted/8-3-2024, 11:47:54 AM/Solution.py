// https://leetcode.com/problems/rearrange-array-elements-by-sign

class Solution(object):
    def rearrangeArray(self, nums):
        array_pos = []
        index = 0
        itr = 0
        array_neg = []
        for i in range(len(nums)):
            if nums[i] > 0:
                array_pos.append(nums[i])
            else:
                array_neg.append(nums[i])
        while index < len(nums):
            nums[index] = array_pos[itr]
            index += 1
            nums[index] = array_neg[itr]
            index += 1
            itr += 1
        return nums

