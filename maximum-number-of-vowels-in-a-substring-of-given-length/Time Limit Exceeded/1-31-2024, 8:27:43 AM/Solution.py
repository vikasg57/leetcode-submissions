// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        
        # for i in range(0, len(s)):
        #     for j in range(i+1, len(s)):
        #         print(i,j)
        
        substrings = []
        n = len(s)
        max_count = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if len(substring) == k:
                    count = 0
                    print(substring)
                    for l in range(0, len(substring)):
                        if substring[l] in vowel:
                            count += 1
                    if count > max_count:
                        max_count = count
        return max_count
