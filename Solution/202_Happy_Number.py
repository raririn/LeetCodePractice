class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Idea: if n is not a happy number, there must be a cycle. -> Two pointers
        '''
        if n == 1:
            return True
        slowpointer = n
        fastpointer = n
        while True:
            slowpointer = self.next(slowpointer)
            fastpointer = self.next(self.next(fastpointer))
            if slowpointer == 1:
                return True
            if slowpointer == fastpointer:
                break
        return slowpointer == 1


    def next(self, n: int) -> int:
        ttl = 0
        while n > 0:
            ttl = ttl + (n % 10) ** 2
            n = n // 10
        return ttl

'''
Runtime: 44 ms, faster than 45.87% of Python3 online submissions for Happy Number.
Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Happy Number.
'''