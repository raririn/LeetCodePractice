class H2O:
    def __init__(self):
        from threading import Semaphore, Barrier
        self.b = Barrier(3)
        self.Hlock = Semaphore(2)
        self.Olock = Semaphore(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.Hlock.acquire()
        self.b.wait()

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.Hlock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.Olock.acquire()
        self.b.wait()

        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.Olock.release()


'''
Runtime: 40 ms, faster than 54.87% of Python3 online submissions for Building H2O.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Building H2O.
'''