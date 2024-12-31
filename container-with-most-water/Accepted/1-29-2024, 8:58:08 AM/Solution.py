// https://leetcode.com/problems/container-with-most-water

class Solution(object):
    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        c_volume = []

        # for i in range(0, len(height)):
        #     for j in range( i + 1, len(height)):
        #         c_width = j - i
        #         c_height = min(height[i], height[j])
        #         c_volume.append(c_width * c_height)
        # return max(c_volume)

        while left < right:
            print(left, right)
            c_width = right - left
            c_height = min(height[right], height[left])
            c_volume.append(c_width * c_height)
            if height[right] < height[left]:
                right -=1
            else:
                left += 1
        return max(c_volume)




