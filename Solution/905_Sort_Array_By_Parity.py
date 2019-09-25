class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        slowptr = 0
        fastptr = len(A) - 1
        while slowptr < fastptr:
            if A[slowptr] & 1:
                A[slowptr], A[fastptr] = A[fastptr], A[slowptr]
                fastptr = fastptr - 1
            if not (A[slowptr] & 1):
                slowptr = slowptr + 1
        return A

'''
Runtime: 96 ms, faster than 56.90% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.4 MB, less than 5.19% of Python3 online submissions for Sort Array By Parity.
'''