// https://leetcode.com/problems/next-greater-element-i

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for i in range(len(nums1)):
            nums1[i] = next_greater.get(nums1[i], -1)

        return nums1