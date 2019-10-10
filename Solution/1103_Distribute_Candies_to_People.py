class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = num_people * [0]
        give = 0
        while candies > 0:
            people[give % num_people] = people[give % num_people] + min(candies, give + 1)
            give = give + 1
            candies = candies - give
        return people

'''
Runtime: 48 ms, faster than 44.83% of Python3 online submissions for Distribute Candies to People.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People.
'''