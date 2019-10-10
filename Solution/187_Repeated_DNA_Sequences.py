class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        def twoWayHash(text):
            ret = 0
            for i in text:
                ret = ret * 27 + (ord(i)-64)
            return ret

        def toStr(hash):
            t = u""
            while hash > 0:
                t = chr(hash % 27+64) + t
                hash = hash // 27
            return t

        d = {}
        ret = []
        for i in range(len(s)-9):
            h = twoWayHash(s[i:i+10])
            if d.get(h, 0) == 1:
                ret.append(toStr(h))
            d[h] = d.get(h, 0) + 1
        return ret

'''
Runtime: 220 ms, faster than 5.05% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 25.7 MB, less than 66.67% of Python3 online submissions for Repeated DNA Sequences.
'''