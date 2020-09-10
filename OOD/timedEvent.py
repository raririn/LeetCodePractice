'''
event x = new event()

x.add_event(3, function(){ cout << "first event" << endl;})
x.add_event(5, function(){ count << "sec event" << endl; })

x.set_timer(4)
x.start_event()
'''

from typing import Callable

class Event():

    def __init__(self):
        self.event_list = []
        self.timer = None

    def add_event(self, time: int, func: Callable[[], None]) -> None:
        self.event_list.append((time, func))
        self.event_list.sort()

    def set_timer(self, time: int) -> None:
        if not self.timer:
            self.timer = time
        else:
            raise Exception('The timer is already set!')
    
    def start_event(self) -> None:
        for event_time, func in self.event_list:
            if event_time >= self.timer:
                func()


if __name__ == "__main__":
    x = Event()
    x.add_event(3, lambda : (print("first event"), None))
    x.add_event(5, lambda : (print("second event"), None))

    x.set_timer(4)
    x.start_event()