class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton
        if x == 0:
            return 0
        x_0 = x/2
        x_n = (x_0 + x/x_0)/2
        t = x_0
        while abs(x_n-t) >= 0.1:
            t = x_n
            x_n = (x_n + x/x_n)/2
        return math.floor(x_n)