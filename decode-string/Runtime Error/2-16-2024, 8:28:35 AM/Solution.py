// https://leetcode.com/problems/decode-string

class Solution(object):
    def decodeString(self, s):
        number_stack = []
        string_stack = []
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                number_stack.append(num)
            elif s[i] == '[':
                string_stack.append('')
                i += 1
            elif s[i] == ']':
                curr_string = string_stack.pop()
                k = number_stack.pop()
                if not string_stack:
                    string_stack.append(curr_string * k)
                else:
                    string_stack[-1] += curr_string * k
                i += 1
            else:
                while i < len(s) and s[i].isalpha():
                    string_stack[-1] += s[i]
                    i += 1
        
        return ''.join(string_stack)
