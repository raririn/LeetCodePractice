class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        shift = 31
        ret = 0
        while shift >= 0:
            ret = (ret << 1) + (n & 1)
            n = n >> 1 # >> 1 is significantly efficient than // 2
            shift = shift - 1
        return ret

'''
Runtime: 12 ms, faster than 94.58% of Python online submissions for Reverse Bits.
Memory Usage: 11.8 MB, less than 39.29% of Python online submissions for Reverse Bits.
'''