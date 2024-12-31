// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_number = float('-inf')
        result = []
        for i in range(0, len(candies)):
            if candies[i] > max_number:
                max_number = candies[i]
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= max_number:
                result.append(True)
            else:
                result.append(False)
        return result