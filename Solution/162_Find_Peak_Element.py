class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        pt = len(nums) // 2
        l = 0
        r = len(nums) - 1
        while l < pt < r:
            if (nums[pt-1] < nums[pt]) and (nums[pt] > nums[pt+1]):
                return pt
            # (pt<left)
            if nums[pt] <= nums[pt-1]:
                # Moves left, update r
                r = pt
                pt -= (pt - l) // 2 if (pt - l) >= 2 else 1
            # (pt>=left) AND (pt<right)
            elif nums[pt] <= nums[pt+1]:
                # Moves right, update l
                l = pt
                pt += (r - pt) // 2 if (r - pt) >= 2 else 1
        return pt
             
