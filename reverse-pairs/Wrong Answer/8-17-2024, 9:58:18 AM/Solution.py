// https://leetcode.com/problems/reverse-pairs

class Solution(object):
    def reversePairs(self, nums):

        count = 0

        for i in range(len(nums)):

            for j in range(i, len(nums)):
                
                if nums[i] > (nums[j] *2):
                    count += 1
        return count 
        