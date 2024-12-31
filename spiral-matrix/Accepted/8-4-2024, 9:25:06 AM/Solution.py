// https://leetcode.com/problems/spiral-matrix

class Solution(object):
    def spiralOrder(self, matrix):
        length = len(matrix[0])
        height = len(matrix)

        left = 0
        right = length - 1
        top = 0
        bottom = height - 1

        vector = []

        while top <= bottom and left <= right:

            for i in range(left, right +1):
                vector.append(matrix[top][i])
            top += 1
            for i in range(top, bottom +1):
                vector.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    vector.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    vector.append(matrix[i][left])
                left += 1
        return vector
