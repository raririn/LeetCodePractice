class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return len([s for s in zip(*A) if list(s) != sorted(s)])

'''
Runtime: 124 ms, faster than 90.56% of Python3 online submissions for Delete Columns to Make Sorted.
Memory Usage: 14.4 MB, less than 8.33% of Python3 online submissions for Delete Columns to Make Sorted.
'''