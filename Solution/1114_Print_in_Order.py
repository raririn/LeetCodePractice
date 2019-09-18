
class Foo:
    def __init__(self):
        from threading import Lock
        self.lock = (Lock(), Lock())
        self.lock[0].acquire()
        self.lock[1].acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.lock[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock[0]:
        # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
        self.lock[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock[1]:
        # printThird() outputs "third". Do not change or remove this line.
            printThird()

'''
Runtime: 68 ms, faster than 65.07% of Python3 online submissions for Print in Order.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Print in Order.
'''