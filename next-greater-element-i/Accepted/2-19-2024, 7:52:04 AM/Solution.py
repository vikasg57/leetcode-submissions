// https://leetcode.com/problems/next-greater-element-i

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        ans = []

        for num in nums1:
            for i in range(0, len(nums2)):
                max_found = False
                if nums2[i] == num:
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > nums2[i]:
                            ans.append(nums2[j])
                            max_found = True
                            break
                    if not max_found:
                        ans.append(-1)
                        break
        return ans