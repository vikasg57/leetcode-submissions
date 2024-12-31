// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution(object):
    def strStr(self, haystack, needle):
        length_check = []
        if needle not in haystack:
            return -1
        else:
            for i in range(0, len(haystack)):
                if needle[0] in haystack:
                    return i