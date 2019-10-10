class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = 'aeiou'
        words = S.split()
        for i, word in enumerate(words):
            if not word[0].lower() in vowel:
                word = word[1:] + word[0]
            words[i] = word + 'ma' + 'a' * (i+1)
        return ' '.join(words)

'''
Runtime: 28 ms, faster than 98.57% of Python3 online submissions for Goat Latin.
Memory Usage: 13.9 MB, less than 11.11% of Python3 online submissions for Goat Latin.
'''