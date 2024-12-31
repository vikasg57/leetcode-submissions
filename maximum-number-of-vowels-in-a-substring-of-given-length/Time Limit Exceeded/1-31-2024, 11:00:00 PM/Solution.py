// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        max_count = 0
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         substring = s[i:j]
        #         if len(substring) == k:
        #             count = 0
        #             for l in range(0, len(substring)):
        #                 if substring[l] in vowel:
        #                     count += 1
        #             if count > max_count:
        #                 max_count = count
        # return max_count
        sub_length = k
        count_list = []
        for i in range(0, n):
            sub = s[i:sub_length]
            sub_length += 1
            if len(sub) == k:
                count = 0
                for l in range(0, len(sub)):
                    if sub[l] in vowel:
                        count += 1
                count_list.append(count)
        return max(count_list)
