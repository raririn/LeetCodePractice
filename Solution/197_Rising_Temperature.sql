# Write your MySQL query statement below
SELECT w1.Id
FROM Weather AS w1, Weather AS w2
WHERE SUBDATE(w1.RecordDate, 1) = w2.RecordDate AND w1.Temperature > w2.Temperature

# Runtime: 541 ms, faster than 5.18% of MySQL online submissions for Rising Temperature.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature. 
