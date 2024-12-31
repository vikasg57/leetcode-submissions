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

        counter = 0
        max_count = 0

        for i in range(0, k):
            if s[i] in vowel:
                counter += 1
        max_count = counter

        for i in range(k, n):
            if s[i] in vowel:
                counter += 1
            if s[i-k] in vowel:
                counter -= 1
            if counter > max_count:
                max_count = counter
        return max_count
