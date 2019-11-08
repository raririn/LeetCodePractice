class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return False
        increaseFlag = False
        decreaseFlag = False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                increaseFlag = True
                if decreaseFlag:
                    return False
            elif A[i] < A[i-1]:
                if not increaseFlag:
                    return False
                decreaseFlag = True
            else:
                return False
        return increaseFlag and decreaseFlag

'''
Runtime: 220 ms, faster than 99.60% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 14 MB, less than 63.16% of Python3 online submissions for Valid Mountain Array.
'''