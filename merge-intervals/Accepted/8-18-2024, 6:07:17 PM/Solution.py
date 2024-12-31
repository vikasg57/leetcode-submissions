// https://leetcode.com/problems/merge-intervals

class Solution(object):
    def merge(self, intervals):

        ans = []

        intervals.sort()

        for i in range(len(intervals)):
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans
