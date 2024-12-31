// https://leetcode.com/problems/product-of-array-except-self

class Solution(object):
    def productExceptSelf(self, nums):
        # i = 0
        # result = []
        # while i < len(nums):
        #     left_prod, right_prod = 1, 1
        #     left, right = i - 1, i + 1
        #     while left >= 0:
        #         left_prod *= nums[left]
        #         left -= 1
        #     while right < len(nums):
        #         right_prod *= nums[right]
        #         right += 1
        #     product = left_prod * right_prod
        #     result.append(product)
        #     i += 1
        # return result

        length = len(nums)
        left = [1] * length
        right = [1] * length
        result = [1] * length

        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]

        for i in range(length -2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(0, length):
            result[i] = left[i] * right[i]
        return result
