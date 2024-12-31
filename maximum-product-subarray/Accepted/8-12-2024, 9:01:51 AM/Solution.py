// https://leetcode.com/problems/maximum-product-subarray

class Solution(object):
    def maxProduct(self, nums):

        if not nums:
            return 0
        max_product = min_product = result = nums[0]
        
        for i in range(1, len(nums)):
            current = nums[i] 
            if current < 0:
                max_product, min_product = min_product, max_product
            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)
            result = max(result, max_product)
        
        return result