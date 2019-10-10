class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies)//2, len(set(candies)))

'''
Runtime: 924 ms, faster than 93.40% of Python3 online submissions for Distribute Candies.
Memory Usage: 15.6 MB, less than 8.33% of Python3 online submissions for Distribute Candies.
'''