// https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):

        obj = {
            "}":"{",
            "]": "[",
            ")":"("
        }

        s = list(s)

        stack = []

        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] ==  "[":
                stack.append(s[i])
            else:
                if not stack:
                    return False            
                if s[i] ==  ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                        continue
                    return False
                elif s[i] ==  "}":
                    if stack and stack[-1] == "{":
                        stack.pop()
                        continue
                    return False
                elif s[i] ==  "]":
                    if stack and stack[-1] == "[":
                        stack.pop()
                        continue
                    return False
        return True
