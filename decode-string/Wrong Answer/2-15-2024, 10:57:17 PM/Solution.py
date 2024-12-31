// https://leetcode.com/problems/decode-string

class Solution(object):
    def decodeString(self, s):


        # Firstly we need to traverse the list if we find number add in number stack
        # If we find the string/bracket add it in string stack
        # When we get our closing bracket ']' means we reached to the innermost bracket
        # We will not add closing bracket into stack instead we will start popping till first opening bracket
        # Then we will get our innermost string we will solve it by multiplying with the uppermost number of number stack and pop the number
        # Then we got our first encoded string then we again push it into string stack and repeat same procedure.

        s= list(s)

        number_stack = []
        string_stack = []
        for i in range(0, len(s)):
            if not s[i].isdigit():
                if s[i] != ']':
                    string_stack.append(s[i])
                else:
                    string = ''
                    while string_stack[-1] != '[':
                        ele = string_stack.pop()
                        print(ele)
                        if ele != '[':
                            string =  ele + string 
                    string_stack.pop()
                    if number_stack:
                        string = string * int(number_stack.pop())
                        
                    string_stack.append(string)
            else:
                number_stack.append(s[i])
        return ''.join(string_stack)
