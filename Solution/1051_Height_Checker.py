class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # probably the worst problem on LeetCode
        return sum([h1!=h2 for h1, h2 in zip(heights, sorted(heights))])


'''
Runtime: 32 ms, faster than 89.32% of Python3 online submissions for Height Checker.
Memory Usage: 13.9 MB, less than 41.85% of Python3 online submissions for Height Checker.
'''