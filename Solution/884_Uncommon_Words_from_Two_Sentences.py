class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d = {}
        for i in A.split(' ') + B.split(' '):
            d[i] = d.get(i) + 1
        ret = []
        for k, v in d.items():
            if v == 1:
                ret.append(k)
        return ret
    
'''
Runtime: 40 ms, faster than 44.68% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 13.7 MB, less than 9.09% of Python3 online submissions for Uncommon Words from Two Sentences.
'''