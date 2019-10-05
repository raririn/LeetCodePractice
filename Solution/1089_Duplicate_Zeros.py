class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr[i+1:] = arr[i:-1]
                if i+1 < len(arr):
                    arr[i+1] = 0
                i = i + 1
            i = i + 1
        return


'''
Runtime: 224 ms, faster than 13.48% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.
'''