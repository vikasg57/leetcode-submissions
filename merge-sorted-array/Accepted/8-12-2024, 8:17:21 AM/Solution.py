// https://leetcode.com/problems/merge-sorted-array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[index]
            index += 1
        nums1.sort()
  