class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        ret = []
        self.DFS(0, target, [], ret)
        return set(ret)

    def DFS(self, index, target, path, ret):
        if target < 0:
            return 
        elif target == 0:
            ret.append(tuple(path))
            return
        else:
            for i in range(index, len(self.candidates)):
                self.DFS(i+1, target-self.candidates[i], path+[self.candidates[i]], ret)

'''
Runtime: 600 ms, faster than 9.01% of Python3 online submissions for Combination Sum II.
Memory Usage: 14 MB, less than 6.52% of Python3 online submissions for Combination Sum II.
'''