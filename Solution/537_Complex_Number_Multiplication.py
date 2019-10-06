class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def multiply(aR: int, aC: int, bR: int, bC: int) -> List[int]:
            rR = aR * bR - aC * bC
            rC = aR * bC + bR * aC
            return [rR, rC]
        aR, aC, bR, bC = map(int, a.replace('i', '').split('+') + b.replace('i', '').split('+'))
        rR, rC = multiply(aR, aC, bR, bC)
        return str(rR) + '+' + str(rC) + 'i'

'''
Runtime: 40 ms, faster than 30.08% of Python3 online submissions for Complex Number Multiplication.
Memory Usage: 13.7 MB, less than 50.00% of Python3 online submissions for Complex Number Multiplication.
'''