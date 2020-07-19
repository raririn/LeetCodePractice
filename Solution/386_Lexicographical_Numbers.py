class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1, n+1)), key = lambda x: str(x))

'''
Runtime: 124 ms, faster than 48.06% of Python3 online submissions for Lexicographical Numbers.
Memory Usage: 20.9 MB, less than 28.66% of Python3 online submissions for Lexicographical Numbers.
'''