// https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        # string = ''.join(str(digit) for digit in digits)
        # string = int(string)
        # string = string + 1
        # string = str(string)
        # string = [int(i) for i in string]
        # return string
    
        length = len(digits) - 1
        for i in range(0, len(digits)):
            digit = digits[length] + 1
            if digit > 9:
                digits[length] = 0
                length -= 1
            else:
                digits[length] = digit
                break
            if length == -1:
                digits.insert(0, 1)

        return digits
