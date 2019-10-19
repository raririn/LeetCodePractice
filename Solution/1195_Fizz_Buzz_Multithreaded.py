import threading
class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.fz = threading.Semaphore(0)
        self.bz = threading.Semaphore(0)
        self.fzbz = threading.Semaphore(0)
        self.num = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        for i in range(self.n//3-self.n//15):
            self.fz.acquire()
            printFizz()
            self.num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        for i in range(self.n//5-self.n//15):
            self.bz.acquire()
            printBuzz()
            self.num.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        for i in range(self.n//15):
            self.fzbz.acquire()
            printFizzBuzz()
            self.num.release()

    # printNumber(x) outputs "x", where x is an integer.            
    def number(self, printNumber):
        for i in range(1, self.n+1):
            self.num.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fzbz.release()
            elif i % 3 == 0:
                self.fz.release()
            elif i % 5 == 0:
                self.bz.release()
            else:
                printNumber(i)
                self.num.release()

'''
Runtime: 52 ms, faster than 77.12% of Python3 online submissions for Fizz Buzz Multithreaded.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Fizz Buzz Multithreaded.
'''