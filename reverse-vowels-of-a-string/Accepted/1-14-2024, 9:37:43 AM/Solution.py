// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution(object):
    def reverseVowels(self, s):
        vowel = 'aeiouAEIOU'

        if s:
            s = list(s)
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] not in vowel:
                    left += 1
                if s[right] not in vowel:
                    right -= 1
                if s[left] in vowel and s[right] in vowel:
                    if not s[left] == s[right]:
                        s[left] ,s[right] = s[right], s[left]
                    left += 1
                    right -= 1
            result = ''.join([elem for elem in s])
            return result


