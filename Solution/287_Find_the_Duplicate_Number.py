class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[0]]
        slow = nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow

# Consider:
# 1. Why there must be a cycle?
# 2. How to find the entry point of the cycle?
#   - Consider in the first run: the slow ptr travels a, fast 2a. The distance from 0 to entry point is x.
#     Then 2a+x = a+x+C, where C is guaranteed to be a multiple of cycle length (likely to be 1)
#     C = a-x, which means another x steps makes the slow pointer to the entry!
#     Why do we need the fast ptr again? It's because we don't record x.
# 3. Why the entry point is the duplicate?


'''
Runtime: 76 ms, faster than 82.37% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 16.3 MB, less than 7.14% of Python3 online submissions for Find the Duplicate Number.
'''