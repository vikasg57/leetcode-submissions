// https://leetcode.com/problems/removing-stars-from-a-string

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        s = list(s)

        for i in range(0, len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop()
        return ''.join(stack)
        