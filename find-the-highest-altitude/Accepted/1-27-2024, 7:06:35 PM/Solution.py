// https://leetcode.com/problems/find-the-highest-altitude

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        add = 0
        max_sum = 0
        for i in range(0, len(gain)):
            add += gain[i]
            if add > max_sum:
                max_sum = add
        return max_sum
        