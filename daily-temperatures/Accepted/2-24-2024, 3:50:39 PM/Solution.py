// https://leetcode.com/problems/daily-temperatures

class Solution(object):
    def dailyTemperatures(self, temperatures):

        stack = []
        ans = []

        for i in range(len(temperatures) - 1, -1, -1):
            if not stack:
                ans.append(0)
            elif stack and stack[-1][0] > temperatures[i]:
                ans.append(stack[-1][1])
            elif stack and stack[-1][0] <= temperatures[i]:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if not stack:
                    ans.append(0)
                else:
                    ans.append(stack[-1][1])
            stack.append((temperatures[i], i))
        ans.reverse()
        for i in range(len(ans)):
            if ans[i] != 0:
                ans[i] = ans[i] - i
        return ans
