class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def time(h, m):
            return 60*h + m
        ret = -1
        tmp = None
        for h1, h2, m1, m2 in itertools.permutations(A):
            h = 10*h1 + h2
            m = 10*m1 + m2
            if h < 24 and m < 60 and time(h, m) > ret:
                ret = time(h, m)
                tmp = (h1, h2, m1, m2)
        if ret < 0:
            return ''
        h1, h2, m1, m2 = tmp[0], tmp[1], tmp[2], tmp[3]
        return str(h1) + str(h2) + ':' + str(m1) + str(m2)

'''
Runtime: 32 ms, faster than 98.37% of Python3 online submissions for Largest Time for Given Digits.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Largest Time for Given Digits.
'''