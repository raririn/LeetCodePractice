class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        
        return [count[num] for num in nums]


'''
Runtime: 56 ms, faster than 87.93% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 13.9 MB, less than 58.52% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
'''