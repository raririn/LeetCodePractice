class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Yuo should know how to remove the number: it's like partition in quick sort.
        while val in nums:
            nums.remove(val)
        return len(nums)

'''
Runtime: 40 ms, faster than 70.22% of Python3 online submissions for Remove Element.
Memory Usage: 14 MB, less than 6.06% of Python3 online submissions for Remove Element.
'''