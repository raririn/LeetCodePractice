class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for k, v in c1.items():
            if not k in c2:
                return False
            if c2[k] < v:
                return False
        return True

'''
Runtime: 48 ms, faster than 80.68% of Python3 online submissions for Ransom Note.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Ransom Note.
'''