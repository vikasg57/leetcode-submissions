// https://leetcode.com/problems/sliding-window-maximum

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        i = 0
        j = 0

        ans = []

        max_int = float('-inf')

        while j < len(nums):
            max_int = max(nums[j], max_int)
            if j- i + 1 < k:
                j += 1
            elif j- i + 1 == k:
                ans.append(max_int)
                j += 1
                i += 1
        return ans


        