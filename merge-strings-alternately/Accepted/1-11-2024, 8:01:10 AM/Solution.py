// https://leetcode.com/problems/merge-strings-alternately

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = ''

        if len(word1) > len(word2):
            long_string = word1
            short_string = word2
        else:
            long_string = word2
            short_string = word1

        for i in range(0, len(short_string)):
            result += word1[i]
            result += word2[i]

        for i in range(len(short_string), len(long_string)):
            result += long_string[i]
        return result