// https://leetcode.com/problems/asteroid-collision

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for i in range(0, len(asteroids)):

            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                if stack[len(stack) - 1] <= asteroids[i]*-1:
                    stack.pop()
        return stack


        