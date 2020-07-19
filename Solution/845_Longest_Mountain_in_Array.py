class Solution:
    def longestMountain(self, A: List[int]) -> int:
        L = len(A)
        maxMountain = 0
        start, end = 0, 0

        while start < L:
            end = start
            if end+1 < L and A[end] < A[end + 1]:
                while end+1 < L and A[end] < A[end+1]:
                    end += 1
                if end+1 < L and A[end] > A[end + 1]:
                    while end+1 < L and A[end] > A[end+1]:
                        end += 1
                    maxMountain = max(maxMountain, (end-start+1))

            start = max(end, start + 1)

        return maxMountain

'''
Runtime: 276 ms, faster than 8.96% of Python3 online submissions for Longest Mountain in Array.
Memory Usage: 14.7 MB, less than 81.82% of Python3 online submissions for Longest Mountain in Array.
'''