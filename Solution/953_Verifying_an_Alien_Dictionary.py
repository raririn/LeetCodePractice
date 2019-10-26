class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key = lambda x: [order.index(i) for i in x])

'''
Runtime: 64 ms, faster than 7.17% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Verifying an Alien Dictionary.
'''