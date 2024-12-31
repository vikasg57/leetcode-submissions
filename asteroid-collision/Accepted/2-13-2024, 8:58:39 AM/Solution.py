// https://leetcode.com/problems/asteroid-collision

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for i in range(0, len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] < asteroids[i]*-1:
                        stack.pop()
                        continue
                    elif stack[-1] == asteroids[i]*-1:
                        stack.pop()
                    break
                else:
                    stack.append(asteroids[i])
        return stack
