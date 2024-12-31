// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_count = 0
        left = 0
        zero_count = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left +=1
            
            max_count = max(max_count, i - left)  
        
        return max_count

                
            

            

        