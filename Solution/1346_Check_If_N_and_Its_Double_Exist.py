class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = dict()
        for i in arr:
            if 2*i in d or i/2 in d:
                return True
            d[i] = 1
        return False
    

'''
Runtime: 52 ms, faster than 85.75% of Python3 online submissions for Check If N and Its Double Exist.
Memory Usage: 13.8 MB, less than 81.13% of Python3 online submissions for Check If N and Its Double Exist.
'''