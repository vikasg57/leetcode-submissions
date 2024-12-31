// https://leetcode.com/problems/string-compression

class Solution(object):
    def compress(self, chars):
        count = 0
        ind = 0
        result = []
        for i in range(0, len(chars)):
            if chars[ind] == chars[i]:
                count += 1
                if i + 1 == len(chars):
                    chars[ind] = chars[i]
                    ind += 1
                    if count > 1:
                        if count < 9:
                            chars[ind] = str(count)
                            ind += 1
                        else:
                            for j in str(count):
                                chars[ind] = str(j)
                                ind += 1
            else:
                chars[ind] = chars[i-1]
                ind += 1
                if count > 1:
                    if count < 9:
                        chars[ind] = str(count)
                        ind += 1
                    else:
                        for j in str(count):
                            chars[ind] = str(j)
                            ind += 1
                count = 1
        return ind
                