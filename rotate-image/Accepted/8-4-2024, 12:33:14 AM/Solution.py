// https://leetcode.com/problems/rotate-image

class Solution(object):
    def rotate(self, matrix):
        
        for i in range(len(matrix)-1):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
