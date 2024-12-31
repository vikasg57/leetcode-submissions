// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution(object):
    def kthDistinct(self, arr, k):
        obj = {}
        for i in range(len(arr)):
            if arr[i] in obj:
                obj[arr[i]] += 1
            else:
                obj[arr[i]] = 1

        distinct = [string for string in arr if obj[string] == 1]
        
        if k <= len(distinct):
            return distinct[k-1]
        else:
            return ""
