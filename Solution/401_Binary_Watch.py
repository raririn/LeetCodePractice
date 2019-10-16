class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return ["%d:%02d" % (h, m) for h in range(0, 12) for m in range(60) if str(bin(h) + bin(m)).count('1') == num]


'''
Runtime: 40 ms, faster than 57.75% of Python3 online submissions for Binary Watch.
Memory Usage: 13.7 MB, less than 9.09% of Python3 online submissions for Binary Watch.
'''