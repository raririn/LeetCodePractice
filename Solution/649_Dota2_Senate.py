class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        d_party = [0] * n
        for i in range(n):
            if senate[i] == 'D':
                d_party[i] = 1
        sum_d = sum(d_party)
        len_n = n
        while (0 in d_party) and (1 in d_party):
            if sum_d >= (2/3*len_n):
                return "Dire"
            elif sum_d <= (1/3*len_n):
                return "Radiant"
            if d_party[0]: # =1, is D
                d_party.remove(0)
                d_party.pop(0)
                d_party.append(1)
            else:
                d_party.remove(1)
                d_party.pop(0)
                d_party.append(0)
                sum_d = sum_d - 1
            len_n = len_n - 1
        if d_party[0]:
            return "Dire"
        else:
            return "Radiant"

'''
Runtime: 204 ms, faster than 17.12% of Python3 online submissions for Dota2 Senate.
Memory Usage: 13.9 MB, less than 50.00% of Python3 online submissions for Dota2 Senate.
'''