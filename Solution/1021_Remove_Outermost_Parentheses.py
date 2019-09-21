class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        c = ''
        flag = 0
        for i in S:
            if i == '(':
                flag = flag + 1
                if flag != 1:
                    c = c + i
            else:
                flag = flag - 1
                if flag != 0:
                    c = c + i
        return c

'''
Runtime: 36 ms, faster than 97.92% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Remove Outermost Parentheses.
'''