class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.toFizz(i) for i in range(1, n+1)]
        
    @staticmethod
    def toFizz(n: int) -> str:
        if n % 15 == 0:
            return "FizzBuzz"
        if n % 3 == 0:
            return "Fizz"
        if n % 5 == 0:
            return "Buzz"
        return str(n)

'''
Runtime: 48 ms, faster than 85.20% of Python3 online submissions for Fizz Buzz.
Memory Usage: 14.8 MB, less than 6.38% of Python3 online submissions for Fizz Buzz.
'''