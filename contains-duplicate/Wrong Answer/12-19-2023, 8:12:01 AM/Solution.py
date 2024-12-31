// https://leetcode.com/problems/contains-duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        
        duplicate = {}

        for i in nums:
            if i not in duplicate:
                duplicate[i] = 1
            else:
                duplicate[i] = duplicate[i] + 1
        
        for j in duplicate.values():
            if j > 1:
                return True
            return False
    