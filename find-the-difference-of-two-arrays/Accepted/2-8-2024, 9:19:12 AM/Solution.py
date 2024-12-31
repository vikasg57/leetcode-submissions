// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution(object):
    def findDifference(self, nums1, nums2):

        intersect = []
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    intersect.append(nums1[i])
        for i in range(0, len(intersect)):
            if intersect[i] in nums1:
                nums1.remove(intersect[i])
            if intersect[i] in nums2:
                nums2.remove(intersect[i])
        return [list(set(nums1)), list(set(nums2))]                