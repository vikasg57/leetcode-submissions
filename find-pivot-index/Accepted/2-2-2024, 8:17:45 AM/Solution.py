// https://leetcode.com/problems/find-pivot-index

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_left = []
        sum_right = []
        add = 0
        add_1 = 0
        for i in range(0, len(nums)):
            add += nums[i]
            sum_left.append(add)
        for i in range(len(nums)-1, -1, -1):
            add_1 += nums[i]
            sum_right.append(add_1)
        sum_right = sum_right[::-1]
        for i in range(len(nums)):
            if sum_left[i] == sum_right[i]:
                result = i
                return i
        return -1
