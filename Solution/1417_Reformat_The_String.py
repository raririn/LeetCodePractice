class Solution:
    def reformat(self, s: str) -> str:
        alphabets = []
        digits = []
        for i in s:
            try:
                int(i)
                digits.append(i)
            except:
                alphabets.append(i)
        
        if abs(len(alphabets) - len(digits)) > 1:
            return ""
        
        if len(alphabets) > len(digits):
            return alphabets[0] + "".join(["".join([i, j]) for i, j in zip(digits, alphabets[1:])])
        
        elif len(alphabets) == len(digits):
            return "".join(["".join([i, j]) for i, j in zip(alphabets, digits)])
        
        else:
            return digits[0] + "".join(["".join([i, j]) for i, j in zip(alphabets, digits[1:])])

'''
Runtime: 72 ms, faster than 20.92% of Python3 online submissions for Reformat The String.
Memory Usage: 14 MB, less than 17.50% of Python3 online submissions for Reformat The String.
'''