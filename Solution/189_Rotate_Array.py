class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], head: int, tail: int) -> List[int]:
            while head < tail:
                nums[head], nums[tail] = nums[tail], nums[head]
                head += 1
                tail -= 1
        
        n = len(nums)
        k %= n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)


'''
Runtime: 104 ms, faster than 26.95% of Python3 online submissions for Rotate Array.
Memory Usage: 15.4 MB, less than 24.86% of Python3 online submissions for Rotate Array.
'''