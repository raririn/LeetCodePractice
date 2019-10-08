class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        t = (sum(B) - sum(A)) // 2 # Since the answer is guaranteed to exist
        A, B = set(A), set(B)
        for i in A:
            if i+t in B:
                return [i, i+t]

'''
Runtime: 468 ms, faster than 17.57% of Python3 online submissions for Fair Candy Swap.
Memory Usage: 16.5 MB, less than 8.33% of Python3 online submissions for Fair Candy Swap.
'''