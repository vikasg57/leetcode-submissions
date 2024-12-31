// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution(object):
    def removeDuplicates(self, nums):
        pointer_1 = 0
        pointer_2 = 1

        for i in range(0, len(nums)):
            print(i)
            print(pointer_1, pointer_2)
            if pointer_2 < len(nums) and nums[pointer_1] == nums[pointer_2]:
                nums.remove(nums[pointer_1])
            else:
                pointer_1 += 1
                pointer_2 = pointer_1 + 1
        return len(nums)