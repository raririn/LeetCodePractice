class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd = 0
        even = 0
        for i in chips:
            if i % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
        return min(odd, even)

'''
Runtime: 40 ms, faster than 67.77% of Python3 online submissions for Play with Chips.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Play with Chips.
'''