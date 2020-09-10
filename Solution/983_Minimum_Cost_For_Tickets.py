class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        from functools import lru_cache
        self.dayset = set(days)
        passes = list(zip([1, 7, 30], costs))

        @lru_cache(days[-1]+1)
        def dp(i):
            if i <= 0 or i > days[-1]:
                return 0
            if i in self.dayset:
                return min(dp(i + duration) + cost for duration, cost in passes)
            else:
                return dp(i+1)
        return dp(1)

'''
Runtime: 44 ms, faster than 76.43% of Python3 online submissions for Minimum Cost For Tickets.
Memory Usage: 14.9 MB, less than 5.09% of Python3 online submissions for Minimum Cost For Tickets.
'''