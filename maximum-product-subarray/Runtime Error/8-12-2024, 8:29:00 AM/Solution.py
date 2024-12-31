// https://leetcode.com/problems/maximum-product-subarray

class Solution(object):
    def maxProduct(self, nums):

        max_product = float('-inf')

        for i in range(len(nums)):
            product = nums[i]
            for j in range(i+1, len(nums)):
                product *=  nums[j]
                max_product = max(product, max_product)

        return max_product