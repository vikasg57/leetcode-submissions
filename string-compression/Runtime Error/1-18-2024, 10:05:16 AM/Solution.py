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
                    result.append(str(chars[i-1]))
                    if count > 1:
                        if count < 9:
                            result.append(str(count))
                        else:
                            [result.append(str(i)) for i in str(count)]
            else:
                result.append(str(chars[ind]))
                if count > 1:
                    result.append(str(count))
                count = 1
                ind = i
        return [char for char in result]
                