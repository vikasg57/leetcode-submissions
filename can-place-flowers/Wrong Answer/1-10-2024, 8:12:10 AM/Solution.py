// https://leetcode.com/problems/can-place-flowers

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        new_flowers = 0
        for i in range(1, len(flowerbed)-1):
            if i - 1 == 0 :
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i - 1] = 1
                    new_flowers += 1
            if  i + 1 == len(flowerbed)-1:
                if flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i + 1] = 1
                    new_flowers += 1
            if flowerbed[i - 1] == 0  and flowerbed[i + 1]== 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                new_flowers += 1
        print(flowerbed)
        if new_flowers >= n:
            return True
