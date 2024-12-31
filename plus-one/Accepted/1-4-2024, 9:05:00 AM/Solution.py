// https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        
        string = ''.join(str(digit) for digit in digits)
        
        string = int(string)
        
        string = string + 1
        
        string = str(string)
        
        string = [int(i) for i in string]
        
        return string
        
