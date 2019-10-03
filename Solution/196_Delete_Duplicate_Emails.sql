# Write your MySQL query statement below
DELETE
FROM Person
WHERE Id NOT IN (
    SELECT *
    FROM (
        SELECT Min(Id)
        FROM Person
        GROUP BY Email
    ) Temp
)

# Runtime: 667 ms, faster than 82.17% of MySQL online submissions for Delete Duplicate Emails.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.