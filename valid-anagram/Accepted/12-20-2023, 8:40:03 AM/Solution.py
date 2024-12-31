// https://leetcode.com/problems/valid-anagram

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        frequency_dict = {}
        for char_s in s:
            if char_s in frequency_dict:
                frequency_dict[char_s] = frequency_dict[char_s] + 1
            else:
                frequency_dict[char_s] = 1
        for char_t in t:
            if char_t in frequency_dict:
                frequency_dict[char_t] = frequency_dict[char_t] - 1
        for frequency in frequency_dict.values():
            if frequency > 0:
                return False
        return True