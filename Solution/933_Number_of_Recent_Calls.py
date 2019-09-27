class RecentCounter:

    def __init__(self):
        from collections import deque
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

'''
Runtime: 332 ms, faster than 88.25% of Python3 online submissions for Number of Recent Calls.
Memory Usage: 18.5 MB, less than 20.00% of Python3 online submissions for Number of Recent Calls.
'''