// https://leetcode.com/problems/equal-row-and-column-pairs

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row_hash = {}
        column_hash = {}


        for i in range(0, len(grid)):
            ele = ''.join(map(str, grid[i]))
            row_hash[ele] = row_hash.get(ele, 0) + 1
            string = ''
            for j in range(0, len(grid[i])):
                string += str(grid[j][i])
            print(string)
            row_hash[string] = row_hash.get(string, 0) + 1
            # column_hash[string] = column_hash.get(string, 0) + 1
            
        result = 0
        for val in row_hash.values():
            if val > 1:
                result += val -1
        return result
