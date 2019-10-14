class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while numbers[p1] + numbers[p2] != target:
            if numbers[p1] + numbers[p2] > target:
                p2 = p2 - 1
            else:
                p1 = p1 + 1
        return [p1+1, p2+1]

'''
Runtime: 72 ms, faster than 86.06% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.1 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.
'''