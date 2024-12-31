// https://leetcode.com/problems/set-matrix-zeroes

class Solution(object):
    def setZeroes(self, matrix):
        row = [1] * len(matrix[0])
        column = [1] * len(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[j] = 0
                    column[i] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[j] == 0 or column[i] == 0:
                    matrix[i][j] = 0
