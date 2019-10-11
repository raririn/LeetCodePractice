from math import ceil
from threading import Semaphore
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.locks = [Semaphore(1), Semaphore(0), Semaphore(0)]
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.locks[0].acquire()
            printNumber(0)
            if i % 2 == 0:
                self.locks[2].release()
            else:
                self.locks[1].release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n//2):
            self.locks[1].acquire()
            printNumber(2*i+2)
            self.locks[0].release()
            
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(ceil(self.n/2)):
            self.locks[2].acquire()
            printNumber(2*i+1)
            self.locks[0].release()

'''
Runtime: 60 ms, faster than 74.60% of Python3 online submissions for Print Zero Even Odd.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Print Zero Even Odd.
'''