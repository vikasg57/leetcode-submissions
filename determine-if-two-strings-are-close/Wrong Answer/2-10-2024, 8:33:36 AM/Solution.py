// https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution(object):
    def closeStrings(self, word1, word2):
        word1 = list(word1)
        word2 = list(word2)

        if len(word1) != len(word2):
            return False
        word1_dict = {}
        word2_dict = {}

        for i in range(0, len(word1)):
            word1_dict[word1[i]] =  word1_dict.get(word1[i], 0) + 1
        
        word1_dict_length_b = len(word1_dict)

        for i in range(0, len(word2)):
            word1_dict[word2[i]] =  word1_dict.get(word2[i], 0) + 1
        
        word1_dict_length_a = len(word1_dict)

        if word1_dict_length_b == word1_dict_length_a:
            return True
        return False