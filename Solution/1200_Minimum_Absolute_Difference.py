class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        diff = float('inf')
        ret = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < diff:
                ret = [[arr[i-1], arr[i]]]
                diff = arr[i] - arr[i-1]
            elif arr[i] - arr[i-1] == diff:
                ret.append([arr[i-1], arr[i]])
        return ret

'''
Runtime: 416 ms, faster than 68.55% of Python3 online submissions for Minimum Absolute Difference.
Memory Usage: 28 MB, less than 100.00% of Python3 online submissions for Minimum Absolute Difference.
'''