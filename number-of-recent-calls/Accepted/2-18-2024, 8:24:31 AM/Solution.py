// https://leetcode.com/problems/number-of-recent-calls

class RecentCounter(object):

    def __init__(self):
        self.requests = deque()
        

    def ping(self, t):

        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        self.requests.append(t)
        return len(self.requests)
