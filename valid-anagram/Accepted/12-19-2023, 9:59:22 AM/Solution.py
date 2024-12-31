// https://leetcode.com/problems/valid-anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        exist = True
        if len(s) == len(t):
            for char_s in range(0, len(s)):
                print(s[char_s])
                if s[char_s] in t:
                    t.remove(s[char_s])
                else:
                    return False
            return True

        else:
            return False
        