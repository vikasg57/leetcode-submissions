// https://leetcode.com/problems/merge-intervals

class Solution(object):
    def merge(self, intervals):

        ans = []

        for i in range(len(intervals) - 1):
            temp = float('-inf')
            if intervals[i][-1] >= intervals[i+1][0]:
                temp = intervals[i][-1]
                intervals[i][-1] = intervals[i+1][-1]
                intervals[i+1].insert(1, 0)
            if isinstance(temp, int) and temp >= intervals[i+1][-1]:
                intervals[i][-1] = temp
            if intervals[i][0] > intervals[i+1][0]:
                intervals[i][0] = intervals[i+1][0]

        ans = [interval for interval in intervals if len(interval) == 2]
        return ans
