// https://leetcode.com/problems/next-greater-element-i

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [self.find_max(num, nums2) for num in nums1]

    def find_max(self, num, nums2):
        for i in range(0, len(nums2)):
            if nums2[i] == num:
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        return nums2[j]
                return -1

                    



