class Solution:


    def findMinFibonacciNumbers(self, k: int) -> int:

        self.f = [1, 1]
        self.ret = 0

        def f(k: int):
            cur = 1
            while cur < k:
                cur = self.f[-1] + self.f[-2]
                self.f.append(cur)
    
        def helper(k: int):
            if k == 0:
                return
            self.ret += 1
            for idx, i in enumerate(self.f):
                if i > k:
                    helper(k-self.f[idx-1])
                    break
        
        f(k)
        helper(k)
        return self.ret

'''
Runtime: 68 ms, faster than 11.98% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
Memory Usage: 14.1 MB, less than 7.32% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
'''