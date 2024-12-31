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
            elif s[i] ==  ")":
                if stack[-1] == "(":
                    stack.pop()
                    continue
                return False
            elif s[i] ==  "}":
                if stack[-1] == "{":
                    stack.pop()
                    continue
                return False
            elif s[i] ==  "]":
                if stack[-1] == "[":
                    stack.pop()
                    continue
                return False
        if len(stack) != 0:
            return False
        return True
