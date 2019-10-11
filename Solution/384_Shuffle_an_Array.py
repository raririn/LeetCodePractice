from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.original = [i for i in nums]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return [i for i in self.original]
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ret = [i for i in self.original]
        for i in range(len(self.original)-1, 0, -1):
            j = randint(0, i)
            ret[i], ret[j] = ret[j], ret[i]
        return ret

    

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
        
'''
Runtime: 380 ms, faster than 68.90% of Python3 online submissions for Shuffle an Array.
Memory Usage: 18.8 MB, less than 100.00% of Python3 online submissions for Shuffle an Array.
'''