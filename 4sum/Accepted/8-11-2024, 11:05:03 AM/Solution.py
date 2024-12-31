// https://leetcode.com/problems/4sum

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()

        triple_list = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for u in range(i+1, len(nums)):
                if u > i+1 and nums[u] == nums[u-1]:
                    continue
                j = u + 1 
                k = len(nums) -1
                while j < k:
                    addition = nums[i] + nums[j] + nums[k] + nums[u]
                    if addition == target:
                        triple = [nums[i], nums[j], nums[k], nums[u]]
                        triple_list.append(triple)
                        k -= 1
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif addition  > target:
                        k -= 1
                    else:
                        j += 1
        return triple_list