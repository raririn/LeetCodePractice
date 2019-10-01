class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        f = {}
        ret = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for num, freq in d.items():
            if freq in f:
                f[freq].append(num)
            else:
                f[freq] = [num]
        for i in range(len(nums), 0, -1):
            if i in f:
                ret = ret + f[i]
                if len(ret) >= k:
                    break
        return ret

'''
Runtime: 140 ms, faster than 11.32% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
'''