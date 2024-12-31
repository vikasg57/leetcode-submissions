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

        word1_dict_length = len(word1_dict)


        for i in range(0, len(word2)):
            word2_dict[word2[i]] =  word2_dict.get(word2[i], 0) + 1

        word2_dict_length = len(word2_dict)


        if word1_dict_length != word2_dict_length:
            return False


        word1_values = word1_dict.values()
        word2_values = word2_dict.values()

        word1_keys = word1_dict.keys()
        word2_keys = word2_dict.keys()

        word1_values.sort()
        word2_values.sort()

        print(word1_keys, word2_keys)

        if set(word1_keys) != set(word2_keys):
            return False

        if word1_values != word2_values:
            return False
        return True