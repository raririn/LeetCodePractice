class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people = sorted([(id_ppl, num) for id_ppl, num in enumerate(groupSizes)], key = lambda x: x[1])
        ret = []
        ptr = 0
        while ptr < len(people):
            head_id, head_capacity = people[ptr][0], people[ptr][1]
            ret.append([i for i, _ in people[ptr:ptr+head_capacity]])
            ptr += head_capacity
        return ret

'''
Runtime: 64 ms, faster than 99.86% of Python3 online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Group the People Given the Group Size They Belong To.
'''