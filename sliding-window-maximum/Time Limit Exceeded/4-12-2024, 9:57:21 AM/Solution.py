// https://leetcode.com/problems/sliding-window-maximum

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        i = 0
        j = 0

        ans = []

        max_int = float('-inf')

        while j < len(nums):
            if max_int <= nums[j]:
                max_int = nums[j]
                max_index = j
            if j- i + 1 < k:
                j += 1
            elif j- i + 1 == k:
                ans.append(max_int)
                if max_index == i:
                    max_int = float('-inf')
                    for idx in range(i + 1, j + 1):
                        if nums[idx] > max_int:
                            max_int = nums[idx]
                            max_index = idx
                j += 1
                i += 1
        return ans
