class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            while b:
                a, b = b, a % b
            return a
        
        g = gcd(p, q)
        p = (p // g) % 2
        q = (q // g) % 2
        if p * q == 1:
            return 1
        else:
            if p == 1:
                return 0
            else:
                return 2

'''
Runtime: 28 ms, faster than 96.15% of Python3 online submissions for Mirror Reflection.
Memory Usage: 13.7 MB, less than 13.33% of Python3 online submissions for Mirror Reflection.
'''