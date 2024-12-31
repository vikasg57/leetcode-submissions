// https://leetcode.com/problems/contains-duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        
        duplicate = {}

        for i in nums:
            if i in duplicate and duplicate[i] > 1:
                retuen True
            duplicate[i] = duplicate.get(i,0) + 1
        return False

        # print(duplicate)
        # print(duplicate.values())
        
        # for j in duplicate.values():
        #     print(j)
        #     if j > 1:
        #         return True
        # return False
    