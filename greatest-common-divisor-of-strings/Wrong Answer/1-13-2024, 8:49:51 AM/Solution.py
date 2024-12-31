// https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        result_str1 = ''
        result_str2 = ''

        for i in range(0, len(str1)):
            if str1[i] not in result_str1:
                result_str1 += str1[i]
        for i in range(0, len(str2)):
            if str2[i] not in result_str2:
                result_str2 += str2[i]
        if result_str1 == result_str2:
            return result_str1
        else:
            return ''       


        # freq_dict = {}
        # for i in range(0, len(str1)):
        #     freq_dict[str1[i]] = freq_dict.get(str1[i], 0) + 1
        # for i in range(0, len(str2)):
        #     if str2[i] in freq_dict and freq_dict[str2[i]] > 0:
        #         freq_dict[str2[i]] -= 1
        #         if str2[i] not in result_str1:
        #             result_str1 += str2[i]
        # for i in freq_dict.keys():
        #     result_str2 += i
        # print(result_str1, result_str2)

