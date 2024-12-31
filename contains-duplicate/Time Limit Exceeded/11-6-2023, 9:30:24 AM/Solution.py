// https://leetcode.com/problems/contains-duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 
        new_list = []
        for i, num in enumerate(nums):
            val = num
            val_ind = i
            for ind, second_num in enumerate(nums):
                if ind == val_ind:
                    continue
                else:
                    if second_num == val:
                        new_list.append(val)
        if new_list:
            return True
        return False
