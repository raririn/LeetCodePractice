class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        e = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        for key, value in d.items():
            if value in e:
                return False
            e[value] = e.get(value, 0) + 1
        return True

'''
Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.
'''