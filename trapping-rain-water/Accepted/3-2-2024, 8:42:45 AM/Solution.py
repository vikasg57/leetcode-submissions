// https://leetcode.com/problems/trapping-rain-water

class Solution(object):
    def trap(self, height):
        mhl = [0]* len(height)
        mhr = [0] * len(height)
        water = [0] * len(height)

        mhl[0] = height[0]
        mhr[len(height)-1] = height[len(height)-1]

        for i in range(1, len(height)):
            if mhl[i-1] > height[i]:
                mhl[i] = mhl[i-1]
            else:
                mhl[i] = height[i]

        for i in range(len(height) -2, -1, -1):
            if mhr[i+1] > height[i]:
                mhr[i] = mhr[i+1]
            else:
                mhr[i] = height[i]

        for i in range(len(height)):
            water[i] = min(mhr[i], mhl[i]) - height[i]
        return sum(water)


