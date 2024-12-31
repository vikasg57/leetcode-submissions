// https://leetcode.com/problems/reverse-pairs

class Solution(object):
    def reversePairs(self, nums):

        return self.merge(nums, 0, len(nums)-1)

    def merge(self, nums, low, high):
        count = 0

        if low >= high:
            return count

        mid = (low + high) // 2

        count += self.merge(nums, low, mid)

        count += self.merge(nums, mid+1, high)

        count += self.count_pairs(nums, low, mid, high)

        self.sort_array(nums, low, mid, high)

        return count

    
    def sort_array(self, nums, low, mid, high):

        temp = []

        left = low

        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    
    def count_pairs(self, nums, low, mid, high):
        count = 0
        right = mid+1

        for i in range(low, mid +1):

            while right <= high and  nums[i] > nums[right] *2:
                right += 1
            count += (right - (mid +1))
        return count
        