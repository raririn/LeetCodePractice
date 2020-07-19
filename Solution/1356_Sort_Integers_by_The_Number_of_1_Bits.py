class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(x: int) -> int:
            ret = 0
            while x > 0:
                ret += x & 1
                x = x >> 1
            return ret
        return sorted(arr, key = lambda x: (countBits(x), x))


'''
Runtime: 80 ms, faster than 39.36% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
'''