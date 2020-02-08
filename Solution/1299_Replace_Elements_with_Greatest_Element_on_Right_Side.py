class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = [i for i in arr]
        ret[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            ret[i] = max(ret[i+1], arr[i+1])
        return ret

'''
Runtime: 120 ms, faster than 25.21% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
'''