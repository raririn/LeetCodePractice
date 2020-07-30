class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        R = len(nums)
        ret = []
        d = dict()
        
        for r in range(R):
            for c in range(len(nums[r])):
                if r+c in d:
                    d[r+c].append(nums[r][c])
                else:
                    d[r+c] = [nums[r][c]]
        
        for k in sorted(d.keys()):
            ret += d[k][::-1]
        
        return ret

'''
Runtime: 1248 ms, faster than 39.78% of Python3 online submissions for Diagonal Traverse II.
Memory Usage: 35.5 MB, less than 78.57% of Python3 online submissions for Diagonal Traverse II.
'''