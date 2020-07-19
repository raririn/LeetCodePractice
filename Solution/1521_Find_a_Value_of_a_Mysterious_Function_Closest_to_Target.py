class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        s1 = set()
        ret = float('max')
        for i in range(len(arr)):
            s2 = set()
            s2.add(arr[i])
            for s in s1:
                s2.add(arr[i] & s)
            for s in s2:
                ret = min(ret, abs(s-target))
            s1 = s2
        return ret

'''
Brilliant solution: https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/discuss/743442/Want-a-O(N)-Video-Solution-Here-is-one-)-clean-code-and-PRACTICE-PROBLEM
Runtime: 1820 ms, faster than 20.00% of Python3 online submissions for Find a Value of a Mysterious Function Closest to Target.
Memory Usage: 28.3 MB, less than 100.00% of Python3 online submissions for Find a Value of a Mysterious Function Closest to Target.
'''