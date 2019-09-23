# Write your MySQL query statement below
SELECT id, movie, description, rating
FROM cinema
WHERE id % 2 = 1 AND description != 'boring'
ORDER BY rating DESC

# Runtime: 120 ms, faster than 82.94% of MySQL online submissions for Not Boring Movies.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Not Boring Movies.