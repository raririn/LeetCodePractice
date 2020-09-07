class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        from collections import deque
        piles = deque(sorted(piles, reverse=True))
        
        ret = 0
        while piles:
            piles.pop()
            piles.popleft()
            ret += piles.popleft()
        
        return ret


'''
Runtime: 676 ms, faster than 71.18% of Python3 online submissions for Maximum Number of Coins You Can Get.
Memory Usage: 26.2 MB, less than 61.77% of Python3 online submissions for Maximum Number of Coins You Can Get.
'''