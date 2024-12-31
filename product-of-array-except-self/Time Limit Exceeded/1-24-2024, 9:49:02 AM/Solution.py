// https://leetcode.com/problems/product-of-array-except-self

class Solution(object):
    def productExceptSelf(self, nums):
        result = []

        left = 0
        right = 0
        i = 0

        left_prod = 1
        right_prod = 1
        product = 1
        result = []
        while i < len(nums):
            left = i - 1
            right = i + 1 
            while left >= 0:
                left_prod *= nums[left]
                left -= 1
            while right < len(nums):
                right_prod *= nums[right]
                right += 1
            product = left_prod * right_prod
            i += 1
            result.append(product)
            product = 1
            left_prod = 1
            right_prod = 1
        return result