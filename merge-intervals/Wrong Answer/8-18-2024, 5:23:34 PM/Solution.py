// https://leetcode.com/problems/merge-intervals

class Solution(object):
    def merge(self, intervals):

        ans = []

        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][-1] = intervals[i+1][-1]
                intervals[i+1].insert(1, 0)
            if intervals[i][0] > intervals[i+1][0]:
                intervals[i][0] = intervals[i+1][0]

        ans = [interval for interval in intervals if len(interval) == 2]
        return ans
