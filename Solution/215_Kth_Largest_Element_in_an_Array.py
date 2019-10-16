class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, pivot):
            count = 0
            cur = 0
            while cur < len(nums) - 1:
                if nums[cur] < nums[pivot]:
                    nums[count], nums[cur] = nums[cur], nums[count]
                    count += 1
                cur += 1
            nums[count], nums[pivot] = nums[pivot], nums[count]
            return count, nums
        
        pos = -1
        k = len(nums) - k
        while len(nums) > 1:
            pos, nums = partition(nums, len(nums)-1)
            if pos > k:
                nums = nums[:pos]
            elif pos < k:
                nums = nums[pos+1:]
                k = k - pos - 1
            else:
                return nums[pos]
        return nums[0]

'''
Runtime: 3156 ms, faster than 5.01% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.8 MB, less than 10.00% of Python3 online submissions for Kth Largest Element in an Array.
'''