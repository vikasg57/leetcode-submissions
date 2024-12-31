// https://leetcode.com/problems/intersection-of-two-arrays

class Solution(object):
    def intersection(self, nums1, nums2):
        intersect = set()

        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    intersect.add(nums1[i])
        return list(intersect)