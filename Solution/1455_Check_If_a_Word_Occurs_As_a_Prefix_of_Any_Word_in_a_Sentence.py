class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        L = len(searchWord)
        words = sentence.split()
        for idx, word in enumerate(words):
            if len(word) < L:
                continue
            if word[:L] == searchWord:
                return idx+1
        return -1

'''
Runtime: 28 ms, faster than 81.59% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
Memory Usage: 14 MB, less than 17.01% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
'''