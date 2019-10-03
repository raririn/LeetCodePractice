SELECT class
FROM courses
GROUP BY class
HAVING COUNT(student) >= 5

# Runtime: 190 ms, faster than 80.47% of MySQL online submissions for Classes More Than 5 Students.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Classes More Than 5 Students.