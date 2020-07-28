class Solution:
    def countLargestGroup(self, n: int) -> int:
        from statistics import multimode
        def digitSum(n: int) -> int:
            ret = 0
            while n:
                ret += n % 10
                n = n // 10
            return ret
        
        L = list(map(range(1, n+1)))
        return len(multimode(L))

'''
Runtime: 80 ms, faster than 94.06% of Python3 online submissions for Count Largest Group.
Memory Usage: 14.1 MB, less than 33.66% of Python3 online submissions for Count Largest Group.
'''