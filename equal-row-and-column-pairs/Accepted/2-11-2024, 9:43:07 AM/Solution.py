// https://leetcode.com/problems/equal-row-and-column-pairs

class Solution(object):
    def equalPairs(self, grid):        
        row_hash = {}
        result = 0

        for i in range(0, len(grid)):
            ele = tuple(grid[i])
            row_hash[ele] = row_hash.get(ele, 0) + 1

        for i in range(0, len(grid)):
            arr_2 = []
            for j in range(0, len(grid)):
                arr_2.append(grid[j][i])
            arr_2 = tuple(arr_2)
            if arr_2 in row_hash and row_hash[arr_2] !=0:
                result += row_hash[arr_2]                     
        return result
