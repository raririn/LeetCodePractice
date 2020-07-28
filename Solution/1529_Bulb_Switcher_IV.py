class Solution:
    def minFlips(self, target: str) -> int:
        flipped = False
        ret = 0
        for i in target:
            if i != str(int(flipped)):
                ret += 1
                flipped = not flipped
        return ret