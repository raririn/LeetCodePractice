class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import bisect
        stones = sorted(stones)
        while len(stones) > 1:
            smashed = stones[-1] - stones[-2]
            stones.pop()
            stones.pop()
            if smashed:
                bisect.insort(stones, smashed)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

'''
Runtime: 36 ms, faster than 83.69% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
'''