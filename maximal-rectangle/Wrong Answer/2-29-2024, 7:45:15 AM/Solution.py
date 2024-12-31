// https://leetcode.com/problems/maximal-rectangle

class Solution(object):
    def maximalRectangle(self, matrix):
        vector = []

        for j in range(0, len(matrix[0])):
            vector.append(int(matrix[0][j]))
        area = self.largestRectangleArea(vector)

        if len(matrix) >1:
            for i in range(1, len(matrix)):
                for j in range(0, len(matrix[i])):
                    if matrix[i][j] == 0:
                        vector[i] = 0
                    else:
                        vector[i] = int(vector[i]) + int(matrix[i][j])
                area = max(area, self.largestRectangleArea(vector))
        return area

    def largestRectangleArea(self, heights):
        #firstly we will find nearest smaller element at right
        # for finding nsr we will start from right (end of list means reverse traversal)
        stack = []
        right = []
        area = []
        pseudo_ind = len(heights)
        for i in range(len(heights) -1, -1, -1):
            if not stack:
                right.append(pseudo_ind)
            elif stack and stack[-1][0] < heights[i]:
                right.append(stack[-1][1])
            elif stack and stack[-1][0] >= heights[i]:
                while stack and stack[-1][0] >= heights[i]:
                    stack.pop()
                if stack:
                    right.append(stack[-1][1])
                else:
                    right.append(pseudo_ind)
            stack.append((heights[i],i))
        right.reverse()

        # then we will find nearest smaller element at left
        # for finding nsl we will start from left means from zero
        stack = []
        left = []
        pseudo_ind = -1
        for i in range(0, len(heights)):
            if not stack:
                left.append(pseudo_ind)
            elif stack and stack[-1][0] < heights[i]:
                left.append(stack[-1][1])
            elif stack and stack[-1][0] >= heights[i]:
                while stack and stack[-1][0] >= heights[i]:
                    stack.pop()
                if stack:
                    left.append(stack[-1][1])
                else:
                    left.append(pseudo_ind)
            stack.append((heights[i],i))
        
        for i in range(len(heights)):
            area_of_element = right[i] - left[i] - 1
            area.append(area_of_element * heights[i])

        return max(area)
