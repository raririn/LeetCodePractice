class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # save max(candies) as a var to save time
        return [i+extraCandies >= max(candies) for i in candies]


'''
Runtime: 68 ms, faster than 9.93% of Python3 online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 13.9 MB, less than 41.34% of Python3 online submissions for Kids With the Greatest Number of Candies.
'''