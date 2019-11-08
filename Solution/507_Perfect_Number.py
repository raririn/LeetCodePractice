class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        '''
        Stupid problem. See the definition and properties of perfect number.
        '''
        if num <= 1:
            return False
        n = 1
        pn = 2**(n-1) * (2**n - 1)
        while pn < num:
            n += 1
            pn = 2**(n-1) * (2**n - 1)
        return pn == num

'''
Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Perfect Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Perfect Number.
'''