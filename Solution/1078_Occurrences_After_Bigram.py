class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        L = len(text)
        ret = []
        for idx, word in enumerate(text):
            if word == first:
                if idx <= L-3 and text[idx+1] == second:
                    ret.append(text[idx+2])
        return ret

'''
Runtime: 28 ms, faster than 78.77% of Python3 online submissions for Occurrences After Bigram.
Memory Usage: 13.8 MB, less than 71.81% of Python3 online submissions for Occurrences After Bigram.
'''