class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ret = []
        for word in words:
            flag = 1
            if word[0].lower() in row1:
                row = row1
            elif word[0].lower() in row2:
                row = row2
            else:
                row = row3
            lowerword = word.lower()
            for i in lowerword:
                if not i in row:
                    flag = 0
                    break
            if flag:
                ret.append(word)
        return ret
    
'''
Runtime: 36 ms, faster than 67.50% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.7 MB, less than 6.67% of Python3 online submissions for Keyboard Row.
'''