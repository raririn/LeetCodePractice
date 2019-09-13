class Solution:

    ''' Cumulative sum is genious!
    
    Consider: [1, 2, 10] equals to add 10 to (1, n), then minus 10 to (3, n).
    Which means, we can make the label only to <1> and <3>. Mark <1> as {10}
    and <3> as {-10}, then doing the cumulative sum gives us the answer.
    
    
    '''
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ret = [0] * n
        for i, j, k in bookings:
            ret[i-1] = ret[i-1] + k
            if j <= n-1:
                ret[j] = ret[j] - k
        for i in range(1, n):
            ret[i] = ret[i] + ret[i-1]
        return ret

'''
Runtime: 1012 ms, faster than 34.88% of Python3 online submissions for Corporate Flight Bookings.
Memory Usage: 27.7 MB, less than 100.00% of Python3 online submissions for Corporate Flight Bookings.
'''