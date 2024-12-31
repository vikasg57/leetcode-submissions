// https://leetcode.com/problems/product-of-array-except-self

class Solution(object):
    def productExceptSelf(self, nums):
        result = []
        i = 0
        product = 1
        result = []
        while i < len(nums):
            left_prod, right_prod = 1, 1
            left, right = i - 1, i + 1
            left = i - 1
            right = i + 1 
            while left >= 0:
                left_prod *= nums[left]
                left -= 1
            while right < len(nums):
                right_prod *= nums[right]
                right += 1
            product = left_prod * right_prod
            result.append(product)
            i += 1
        return result