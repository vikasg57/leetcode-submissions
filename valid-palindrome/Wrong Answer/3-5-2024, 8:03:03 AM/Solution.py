// https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        sanitized = ''
        for i in range(0, len(s)):
            if s[i].isalpha():
                sanitized += s[i]
        if len(sanitized) == 1:
            return False
        left = 0
        right = len(sanitized) - 1
        ans = True

        while left < right:
            if sanitized[left] == sanitized[right]:
                left += 1
                right -= 1
            else:
                ans = False
                left += 1
                right -= 1
        return ans            