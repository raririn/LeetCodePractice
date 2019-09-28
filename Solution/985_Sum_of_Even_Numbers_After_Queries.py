class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        evenlist = [not(i % 2) for i in A]
        sumEven = sum(map(lambda x, y: x*y, A, evenlist))
        ret = []
        for query in queries:
            if (evenlist[query[1]] and (query[0] % 2)): # Even + Odd, a number should be removed from evenlist
                evenlist[query[1]] = False
                sumEven = sumEven - A[query[1]]
            elif (not evenlist[query[1]] and (query[0] % 2)):   # Odd + Odd
                evenlist[query[1]] = True
                sumEven = sumEven + A[query[1]] + query[0]
            elif (evenlist[query[1]]) and (not (query[0] % 2)): # Even + Even
                sumEven = sumEven + query[0]
            A[query[1]] = A[query[1]] + query[0]
            ret.append(sumEven)
        return ret

'''
Runtime: 620 ms, faster than 15.34% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 19.8 MB, less than 5.88% of Python3 online submissions for Sum of Even Numbers After Queries.
'''