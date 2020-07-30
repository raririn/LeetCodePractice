class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_num, min_num = float('-inf'), float('inf')

        for i in '0123456789':
            for j in '0123456789':
                cur = num.replace(i, j)
                if cur[0] == '0' or int(cur) == 0:
                    continue
                max_num = max(max_num, int(cur))
                min_num = min(min_num, int(cur))
        
        return max_num - min_num


'''
Runtime: 44 ms, faster than 32.78% of Python3 online submissions for Max Difference You Can Get From Changing an Integer.
Memory Usage: 13.8 MB, less than 68.00% of Python3 online submissions for Max Difference You Can Get From Changing an Integer.
'''