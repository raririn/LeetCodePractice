from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.locks = [Semaphore(1), Semaphore(0)]


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.locks[0].acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.locks[1].release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.locks[1].acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.locks[0].release()

'''
Runtime: 88 ms, faster than 52.07% of Python3 online submissions for Print FooBar Alternately.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Print FooBar Alternately.
'''