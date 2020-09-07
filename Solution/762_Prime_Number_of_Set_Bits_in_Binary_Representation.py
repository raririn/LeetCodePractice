class Solution:

    def getPrimes(self, max_num):
        primes = set()
        arr = [True] * (max_num+1)
        arr[0] = False
        for i in range(2, max_num+1):
            if arr[i]:
                cur = i
                for j in range(cur, max_num+1, cur):
                    arr[j] = False
                arr[cur] = True
        for i in range(2, max_num+1):
            if arr[i]:
                primes.add(i)
        return primes


    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = self.getPrimes(len(bin(R)[2:]))
        ret = 0
        for i in range(L, R+1):
            ret += (sum(list(map(int, list(bin(i)[2:])))) in primes)
        return ret

'''
Runtime: 1436 ms, faster than 12.15% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
Memory Usage: 13.9 MB, less than 42.53% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
'''