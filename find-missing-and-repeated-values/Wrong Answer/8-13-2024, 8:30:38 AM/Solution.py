// https://leetcode.com/problems/find-missing-and-repeated-values

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):

        nums = [ele for row in grid for ele in row ]
        
        nums.sort()
        ans = [0] * 2
        for i in range(len(nums)-1):
            if nums[0] != 1:
                ans.append(nums[0])
            if nums[i] + 1 != nums[i+1]:
                if nums[i] == nums[i+1]:
                    ans[0] = nums[i]
                else:
                    ans[1] = nums[i] + 1
        if ans[1] == 0:
            ans[1] = len(nums)
        return ans
