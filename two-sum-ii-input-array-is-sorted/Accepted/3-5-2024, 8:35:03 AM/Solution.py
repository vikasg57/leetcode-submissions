// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution(object):
    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1
        ans = []
        while left < right:
            print(left, right)
            target_sum = numbers[left] + numbers[right]

            if target_sum > target:
                right -= 1
            elif target_sum < target:
                left += 1
            else:
                ans.append(left + 1)
                ans.append(right + 1)
                break
        return ans        