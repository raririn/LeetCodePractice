class Solution:
    def customSortString(self, S: str, T: str) -> str:
        def helper(x:str) -> str:
            if x in S:
                return S.index(x)
            else:
                return -1
        return ''.join(sorted(list(T), key = helper))


'''
Runtime: 28 ms, faster than 68.39% of Python3 online submissions for Custom Sort String.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Custom Sort String.
'''