class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tail = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if (i + nums[i]) >= tail:
                tail = i
        
        return tail == 0


'''
Runtime: 76 ms, faster than 99.73% of Python3 online submissions for Jump Game.
Memory Usage: 15.7 MB, less than 87.97% of Python3 online submissions for Jump Game.
'''