// https://leetcode.com/problems/string-compression

class Solution(object):
    def compress(self, chars):
        count = 1
        ind = 0
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                chars[ind] = chars[i-1]
                ind += 1
                if count > 1:
                    if count < 9:
                        chars[ind] = str(count)
                        ind += 1
                    else:
                        for digit in str(count):
                            chars[ind] = digit
                            ind += 1
                count = 1 

        chars[ind] = chars[-1]
        ind += 1
        if count > 1:
            if count < 9:
                chars[ind] = str(count)
                ind += 1
            else:
                for digit in str(count):
                    chars[ind] = digit
                    ind += 1

        return ind

                