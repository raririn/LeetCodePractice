class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        '''
        A pure math question.

        Intuitively, for two integers p, q, as long as they are co-prime,
        we can always find a, b such ap+bq = 1 (Think of why?)

        However, for p and q having gcd(p, q) > 1, let's say, 2.
        Then for any integers a, b, we have 2 | ap+bq. Then the 
        result can't be 1!

        The hard part is, how to prove that the condition holds for all
        co-prime integers. Take a look at Bezout's Lemma.
        '''
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            while b:
                a, b = b, a % b
            return a
        ret = nums[0]
        for i in nums:
            ret = gcd(ret, i)
        return ret == 1

'''
Runtime: 364 ms, faster than 33.33% of Python3 online submissions for Check If It Is a Good Array.
Memory Usage: 24.1 MB, less than 100.00% of Python3 online submissions for Check If It Is a Good Array.
'''