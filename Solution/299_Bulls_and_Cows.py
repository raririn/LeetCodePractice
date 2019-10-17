class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = {}
        c = []
        bulls, cows = 0, 0
        p1, p2 = 0, 0
        while p1 < min(len(secret), len(guess)):
            if secret[p1] == guess[p1]:
                bulls += 1
            else:
                d[secret[p1]] = d.get(secret[p1], 0) + 1
                c.append(guess[p1])
            p1 += 1
        if p1 < len(guess):
            c = c + [i for i in guess[p1:]]
        if p1 < len(secret):
            for i in secret[p1:]:
                d[secret[i]] = d.get(secret[i], 0) + 1
        for i in c:
            g = d.get(i, 0)
            if g:
                cows += bool(g)
                d[i] -= 1
        return "%dA%dB" % (bulls, cows)

'''
Runtime: 60 ms, faster than 20.30% of Python3 online submissions for Bulls and Cows.
Memory Usage: 13.8 MB, less than 25.00% of Python3 online submissions for Bulls and Cows.
'''