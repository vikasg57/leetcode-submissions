// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution(object):
    def intersect(self, nums1, nums2):

        short_list_dict = {}

        ans_list = []
        
        short_list = None
        long_list = None

        if len(nums1) < len(nums2):
            short_list = nums1
            long_list = nums2
        else:
            short_list = nums2
            long_list = nums1

        for i in range(0, len(short_list)):
            short_list_dict[short_list[i]] = short_list_dict.get(short_list[i], 0) + 1

        for i in range(0, len(long_list)):
            if long_list[i] in short_list_dict and short_list_dict[long_list[i]] > 0:
                short_list_dict[long_list[i]] -= 1
                ans_list.append(long_list[i])
        return ans_list

