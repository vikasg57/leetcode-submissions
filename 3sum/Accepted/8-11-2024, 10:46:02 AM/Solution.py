// https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):

        nums.sort()

        triple_list = []

        i = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1 
            k = len(nums) -1
            while j < k:
                addition = nums[i] + nums[j] + nums[k]
                if addition == 0:
                    triple = [nums[i], nums[j], nums[k]]
                    triple_list.append(triple)
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif addition  > 0:
                    k -= 1
                else:
                    j += 1
        return triple_list