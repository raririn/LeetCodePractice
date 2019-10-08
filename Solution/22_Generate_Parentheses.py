class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        self.generate(n, n, '', ret)
        return ret

    def generate(self, left: int, right: int, res: str, ret: []) -> List[str]:
        if left == 0:
            ret.append(res + ')' * right)
            return
        if left == right:
            self.generate(left-1, right, res + '(', ret)
        elif left < right:
            self.generate(left-1, right, res + '(', ret)
            self.generate(left, right-1, res + ')', ret)

'''
Runtime: 56 ms, faster than 12.58% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.2 MB, less than 6.67% of Python3 online submissions for Generate Parentheses.
'''