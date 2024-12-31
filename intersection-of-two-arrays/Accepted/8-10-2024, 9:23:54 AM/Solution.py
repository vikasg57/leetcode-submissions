// https://leetcode.com/problems/intersection-of-two-arrays

class Solution(object):
    def intersection(self, nums1, nums2):
        p_1 = 0
        p_2 = 0
        vector = []

        nums1.sort()
        nums2.sort()

        while p_1 < len(nums1) and p_2 < len(nums2):

            if nums1[p_1] == nums2[p_2]:
                if not vector or nums1[p_1] != vector[-1]:
                    vector.append(nums1[p_1])
                p_1 += 1
                p_2 += 1
            elif nums1[p_1] < nums2[p_2]:
                p_1 += 1
            else:
                p_2 += 1
        return vector
