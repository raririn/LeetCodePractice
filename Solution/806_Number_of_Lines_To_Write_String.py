class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        count = 0
        line = 1
        for i in S:
            count = count + widths[ord(i) - ord('a')]
            if count > 100:
                line = line + 1
                count = widths[ord(i) - ord('a')]
            elif count == 100:
                line = line + 1
                count = 0
        return [line, count]
    
'''
Runtime: 40 ms, faster than 55.48% of Python3 online submissions for Number of Lines To Write String.
Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for Number of Lines To Write String.
'''