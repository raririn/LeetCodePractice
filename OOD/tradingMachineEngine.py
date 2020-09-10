from math import floor, ceil
from collections import Counter
from typing import List, Tuple

class TradingMachineEngine():

    def __init__(self):
        self.pile_list = []
    
    def add_pile(self, pile_name: str, pile_vol: int) -> None:
        self.pile_list.append([pile_name, pile_vol])
    
    def match(self, units: int) -> List[Tuple[str, int]]:
        step_one_units = floor(0.4 * units)
        step_two_units = units - step_one_units


        res = dict()

        # Step one matching: FIFO
        while step_one_units > 0 and self.pile_list:
            pile_name, pile_vol = self.pile_list.pop()
            step_one_units -= pile_vol
            res[pile_name] = res.get(pile_name, 0) + pile_vol
        
        if step_one_units < 0:
            res[pile_name] = res.get(pile_name, 0) + step_one_units
            self.pile_list.append([pile_name, -step_one_units])
        

        # Step two matching: Pro Rata
        vol_counter = dict()
        vol_sum = 0
        for pile_name, pile_vol in self.pile_list:
            vol_counter[pile_name] = pile_vol
            vol_sum += pile_vol

        if vol_sum <= step_two_units:
            for pile_name, pile_vol in self.pile_list:
                res[pile_name] = res.get(pile_name, 0) + pile_vol
        
        else:
            for idx in range(len(self.pile_list)):
                pile_name, _ = self.pile_list[idx]
                allocate_amount = ceil(step_two_units * vol_counter[pile_name] / vol_sum)
                res[pile_name] = res.get(pile_name, 0) + allocate_amount
                self.pile_list[idx] = [pile_name, self.pile_list[idx][1] - allocate_amount]
        
        return [(k, v) for k, v in res.items()]


if __name__ == "__main__":
    tme = TradingMachineEngine()
    tme.add_pile("A", 14)
    tme.add_pile("B", 20)
    print(tme.match(10))