// https://leetcode.com/problems/is-subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        string = ''
        index = 0
        for i in range(0, len(t)):
            if t[i] == s[index]:
                string += s[index]
                index += 1
        if string == s:
            return True
        return False
