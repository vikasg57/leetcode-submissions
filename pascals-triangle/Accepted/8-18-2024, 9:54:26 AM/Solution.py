// https://leetcode.com/problems/pascals-triangle

class Solution(object):
    def generate(self, numRows):
        pascals = []

        for i in range(1, numRows+1):
            row = self.generate_rows(i)
            pascals.append(row)
        return pascals

    
    def generate_rows(self, row):
        res = 1
        ans = [1]

        for col in range(1, row):
            res *= (row -col)
            res = res // col
            ans.append(res)
        return ans
