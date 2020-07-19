class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if not k:
            return num
        elif k > n*(n-1)/2:
            return "".join(sorted(list(num)))
        
        for i in range(10):
            # Find the first smallest digit
            idx = num.find(str(i))

            if 0 <= idx <= k:
                return self.minInteger(num[:idx] + num[idx+1:], k = idx)

'''
Runtime: 76 ms, faster than 100.00% of Python3 online submissions for Minimum Possible Integer After at Most K Adjacent Swaps On Digits.
Memory Usage: 46.8 MB, less than 100.00% of Python3 online submissions for Minimum Possible Integer After at Most K Adjacent Swaps On Digits.
'''