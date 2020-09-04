class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        return "".join([k*v for k, v in c.most_common()])


'''
Runtime: 32 ms, faster than 97.40% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 14.9 MB, less than 89.02% of Python3 online submissions for Sort Characters By Frequency.
'''