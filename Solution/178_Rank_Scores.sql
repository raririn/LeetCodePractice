# Write your MySQL query statement below
SELECT Score, (
    SELECT COUNT(DISTINCT score)
    FROM Scores AS s1
    WHERE s1.Score >= s2.Score
) Rank
FROM Scores AS s2
ORDER BY Score DESC

# Runtime: 638 ms, faster than 24.24% of MySQL online submissions for Rank Scores.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.
