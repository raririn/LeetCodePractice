# Write your MySQL query statement below
UPDATE salary
SET sex = (CASE WHEN sex = 'f' THEN 'm' ELSE 'f' END)

# Runtime: 142 ms, faster than 81.33% of MySQL online submissions for Swap Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Swap Salary.
