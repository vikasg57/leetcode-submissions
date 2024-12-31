// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution(object):
    def reverseVowels(self, s):
        vowel = ['a', 'e', 'i', 'o', 'u']
        temp = ''

        if s:
            s = list(s)
            temp = ''
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] not in vowel:
                    left += 1
                if s[right] not in vowel:
                    right -= 1
                if s[left] and s[right] in vowel:
                    temp = s[left]
                    s[left] = s[right]
                    s[right] = temp
                    left += 1
                    right -= 1
            result = ''.join([elem for elem in s])
            return result


