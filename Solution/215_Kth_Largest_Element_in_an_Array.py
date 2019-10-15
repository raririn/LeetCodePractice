class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = 0
        while pos != k:
            median = nums[len(nums)//2]
            pos = 0
            for i in nums:
                if i <= median:
                    pos = pos + 1
            nums[pos], nums[median] = nums[median], nums[pos]
            if pos > k:
                num = num[:pos]
            elif pos < k:
                num = [pos:]
                k = k - pos
            else:
                return num[pos]