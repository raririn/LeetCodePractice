class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        a = set("".join(MORSE[ord(i) - ord('a')] for i in w) for w in words)
        return len(a)

'''
Runtime: 48 ms, faster than 13.60% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 13.5 MB, less than 5.00% of Python3 online submissions for Unique Morse Code Words.
'''