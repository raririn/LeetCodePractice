class Solution:
    def freqAlphabets(self, s: str) -> str:
        d1, d2 = {}, {}
        for i in range(9):
            d1[str(i+1)] = chr(ord('a')+i)
        for i in range(9, 26):
            d2[str(i+1)+'#'] = chr(ord('a')+i)
        
        for k, v in d2.items():
            s = s.replace(k, v)
        for k, v in d1.items():
            s = s.replace(k, v)
        
        return s

'''
Runtime: 20 ms, faster than 98.77% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
Memory Usage: 13.9 MB, less than 27.91% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
'''