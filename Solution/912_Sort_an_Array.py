class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge sort
        nums = [[i] for i in nums]
        while len(nums) > 1:
            nums.append(self.merge(nums[0], nums[1]))
            nums.pop(0)
            nums.pop(0)
        return nums[0]
        
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p1 = 0
        p2 = 0
        ret = []
        if len(arr1) == 0:
            return arr2
        if len(arr2) == 0:
            return arr1
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] < arr2[p2]:
                ret.append(arr1[p1])
                p1 = p1 + 1
            else:
                ret.append(arr2[p2])
                p2 = p2 + 1
        ret = ret + arr1[p1:] + arr2[p2:]
        return ret

'''
Runtime: 864 ms, faster than 5.21% of Python3 online submissions for Sort an Array.
Memory Usage: 21 MB, less than 7.14% of Python3 online submissions for Sort an Array.
'''