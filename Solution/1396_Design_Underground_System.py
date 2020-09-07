class UndergroundSystem:

    def __init__(self):
        self.finished = dict()
        self.checkin = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, start_t = self.checkin[id]
        del self.checkin[id]
        self.finished[(startStation, stationName)] = self.finished.get((startStation, stationName), []) + [t - start_t]

    @staticmethod
    def avg(l):
        return sum(l) / len(l)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg(self.finished[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

'''
Runtime: 268 ms, faster than 50.87% of Python3 online submissions for Design Underground System.
Memory Usage: 23 MB, less than 71.94% of Python3 online submissions for Design Underground System.
'''