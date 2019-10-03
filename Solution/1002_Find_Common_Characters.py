class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []
        elif len(A) == 1:
            return [i for i in A[0]]
        d = list(A[0])
        for word in A:
            temp = []
            for char in word:
                if c in d:
                    d.remove(d)
                    temp.append(d)
            d = temp
        return d

'''
Runtime: 60 ms, faster than 59.70% of Python3 online submissions for Find Common Characters.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Find Common Characters.
'''