// https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution(object):
    def maxOperations(self, nums, k):
        # result = 0
        # for i in range(0, len(nums)):
        #     if nums[i] != 0:
        #         num = k - nums[i]
        #         for j in range(i+1, len(nums)):
        #             if nums[j]!=0 and nums[j] == num:
        #                 result += 1
        #                 nums[j] = 0
        #                 nums[i] = 0
        #                 break
        # return result

        nums.sort()
        left = 0
        right = len(nums) - 1
        result = 0

        while left < right:
            if nums[left] != 0:
                if nums[right] + nums[left] == k :
                    result += 1
                    nums[left] = 0
                    nums[right] = 0
                    left += 1
                    right -= 1
                elif nums[right] + nums[left] > k:
                    right -= 1
                else:
                    left += 1
        return result