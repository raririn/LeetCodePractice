class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        if n <= 2:
            return 0
        sieve = [1] * (n+1)
        sieve[0] = 0
        sieve[1] = 0
        sieve[-1] = 0
        for i in range(int(math.sqrt(n)) + 1):
            if sieve[i]:
                for j in range(2, (n // i) + 1):
                    #print(i, " remove ", i*j)
                    sieve[i*j] = 0
                    
        #print(sieve)
        return sum(sieve)

'''
Runtime: 548 ms, faster than 56.69% of Python3 online submissions for Count Primes.
Memory Usage: 25.2 MB, less than 79.31% of Python3 online submissions for Count Primes.
'''