class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            while b:
                a, b = b, a % b
            return a

        c = collections.Counter(deck)
        g = c[deck[0]]
        for k, v in c.items():
            g = gcd(g, v)
            if g == 1:
                return False
        return True

'''
Runtime: 136 ms, faster than 99.78% of Python3 online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for X of a Kind in a Deck of Cards.
'''