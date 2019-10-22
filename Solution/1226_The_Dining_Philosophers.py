from threading import Semaphore
class DiningPhilosophers:
    lock = Semaphore(1)

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # Cheating: don't let other philosopher eat.
        self.lock.acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.lock.release()

'''
Runtime: 120 ms, faster than 35.90% of Python3 online submissions for The Dining Philosophers.
Memory Usage: 16.5 MB, less than 100.00% of Python3 online submissions for The Dining Philosophers.
'''