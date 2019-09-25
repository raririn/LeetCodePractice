class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        remaining = sorted([n for n in arr1 if n not in arr2])
        arrR = {}
        for i in range(len(arr2)):
            arrR[arr2[i]] = i
        for i in range(len(arr1)):
            arr1[i] = (arr1[i], arrR.get(arr1[i], -1))
        return sorted([n for n in arr1 if n[1] >= 0], key = lambda x: x[1]， reverse = True)
        
'''
Runtime: 52 ms, faster than 31.73% of Python3 online submissions for Relative Sort Array.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Relative Sort Array.
'''