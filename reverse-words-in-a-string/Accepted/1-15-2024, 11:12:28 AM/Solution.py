// https://leetcode.com/problems/reverse-words-in-a-string

class Solution(object):
    def reverseWords(self, s):
    
        s = s.split(' ')
        p_1 = -1
        p_2 = len(s) - 1

        clean_list = []

        while p_1 < p_2:
            if s[p_2] != '':
                clean_list.append(s[p_2])
            p_2 -= 1
            # p_1 += 1
        return ' '.join(clean_list)