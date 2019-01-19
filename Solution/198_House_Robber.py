class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums):
            [max_l3, max_l2, max_l1, max_cur] = [0] * 4
            for num in nums:
                max_l3 = max_l2
                max_l2 = max_l1
                max_l1 = max_cur
                max_cur = max(max_l3 + num, max_l2 + num, max_l1)
            return max(max_l1, max_cur)
        else:
            return 0