// https://leetcode.com/problems/unique-number-of-occurrences

class Solution(object):
    def uniqueOccurrences(self, arr):
        
        value_dict = {}
        for i in range(0, len(arr)):
            value_dict[arr[i]] = value_dict.get(arr[i], 0) + 1
        values = list(set(value_dict.values()))
        keys = list(value_dict.keys())

        if len(keys) == len(values):
            return True
        return False