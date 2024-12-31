// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution(object):
    def reverseVowels(self, s):
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        temp = ''

        if s:
            s = list(s)
            left = 0
            right = len(s) - 1
            while left < right:
                print('left', left, s[left])
                print('right', right, s[right])
                if s[left] not in vowel:
                    left += 1
                if s[right] not in vowel:
                    right -= 1
                if s[left] and s[right] in vowel:
                    if not s[left] == s[right]:
                        s[left] ,s[right] = s[right], s[left]
                    left += 1
                    right -= 1
            result = ''.join([elem for elem in s])
            return result


