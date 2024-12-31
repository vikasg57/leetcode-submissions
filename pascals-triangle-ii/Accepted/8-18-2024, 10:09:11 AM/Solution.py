// https://leetcode.com/problems/pascals-triangle-ii

class Solution(object):
    def getRow(self, rowIndex):
        res = 1
        ans = [1]

        for col in range(1, rowIndex + 1):
            res *= (rowIndex - col + 1)
            res //= col
            ans.append(res)
        return ans
        