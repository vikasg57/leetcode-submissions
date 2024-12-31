// https://leetcode.com/problems/online-stock-span

class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.answer = []
        self.ind = -1
        

    def next(self, price):
        self.ind  += 1
        if not self.stack:
            self.answer.append(-1)
        elif self.stack and self.stack[-1][0] > price: 
            self.answer.append(self.stack[-1][1])
        elif self.stack and self.stack [-1][0] <= price:
            while self.stack and self.stack [-1][0] <= price:
                self.stack.pop()
            if not self.stack:
                self.answer.append(-1)
            else:
                self.answer.append(self.stack[-1][1])
        self.stack.append((price, self.ind))
        print(self.answer)
        print(self.ind)
        return self.ind - self.answer[self.ind]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)