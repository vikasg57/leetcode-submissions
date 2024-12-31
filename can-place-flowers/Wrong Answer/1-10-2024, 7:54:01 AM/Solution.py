// https://leetcode.com/problems/can-place-flowers

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        new_flowers = 0
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i - 1] == 0  and flowerbed[i + 1]== 0 and flowerbed[i] == 0:
                new_flowers += 1
        if new_flowers >= n:
            return True
