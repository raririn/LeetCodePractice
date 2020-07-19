class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            cur = nums[i]
            if cur in d:
                if (i - d[cur]) <= k:
                    return True
            d[cur] = i
        return False

'''
Runtime: 168 ms, faster than 7.21% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 21.5 MB, less than 59.50% of Python3 online submissions for Contains Duplicate II.
'''