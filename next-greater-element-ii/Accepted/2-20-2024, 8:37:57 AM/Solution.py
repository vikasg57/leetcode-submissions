// https://leetcode.com/problems/next-greater-element-ii

class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        N = len(nums)
        ans = [-1] * N  # Initialize ans with -1

        for i in range(2 * N - 1, -1, -1):
            idx = i % N  # Use modulo to handle circularity

            while stack and stack[-1] <= nums[idx]:
                stack.pop()

            if stack:
                ans[idx] = stack[-1]

            stack.append(nums[idx])

        return ans
