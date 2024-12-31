// https://leetcode.com/problems/is-subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        string = ''
        for i in range(0, len(t)):
            for j in range(0, len(s)):
                if t[i] == s[j]:
                    string += t[i]
        if string == s:
            return True
        return False
        