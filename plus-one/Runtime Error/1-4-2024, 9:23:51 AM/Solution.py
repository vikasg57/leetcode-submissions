// https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        # string = ''.join(str(digit) for digit in digits)
        # string = int(string)
        # string = string + 1
        # string = str(string)
        # string = [int(i) for i in string]
        # return string
        
        if len(digits) > 1:
            digits[len(digits) -1] = digits[len(digits) -1] + 1
        else:
            digits[0], digits[1] = digits[0] + 1
        return digits
        
                
