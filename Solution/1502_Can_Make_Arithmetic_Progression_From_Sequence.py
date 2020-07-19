class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        last = arr[1]
        diff = arr[1] - arr[0]
        for i in arr[2:]:
            if i - last != diff:
                return False
            last = i
        return True

'''
Runtime: 36 ms, faster than 66.67% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
'''