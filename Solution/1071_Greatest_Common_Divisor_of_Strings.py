class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # The same as gcd algorithm for integers.
        l1 = len(str1)
        l2 = len(str2)
        if l1 < l2:
            str1, str2 = str2, str1
        if str1[:l2] != str2:
            return False
        
        str1 = str1[l2:]
        if len(str1) == 0:
            return str2
        return self.gcdOfStrings(str1, str2)

'''
Runtime: 28 ms, faster than 98.83% of Python3 online submissions for Greatest Common Divisor of Strings.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Greatest Common Divisor of Strings.
'''