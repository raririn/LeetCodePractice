class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque

        ret = [0] * len(deck)
        idx_q = deque(range(len(deck)))

        for card in sorted(deck):
            ret[idx_q.popleft()] = card
            if idx_q:
                idx_q.append(idx_q.popleft())
        
        return ret


'''
Runtime: 48 ms, faster than 71.05% of Python3 online submissions for Reveal Cards In Increasing Order.
Memory Usage: 14.2 MB, less than 5.09% of Python3 online submissions for Reveal Cards In Increasing Order.
'''