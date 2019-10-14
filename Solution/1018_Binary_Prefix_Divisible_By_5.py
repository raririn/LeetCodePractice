class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n = 0
        ret = []
        for i in A:
            n = 2 * n + i
            if n % 5 == 0:
                ret.append(True)
            else:
                ret.append(False)
        return ret

'''
Runtime: 340 ms, faster than 35.58% of Python3 online submissions for Binary Prefix Divisible By 5.
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Binary Prefix Divisible By 5.
'''