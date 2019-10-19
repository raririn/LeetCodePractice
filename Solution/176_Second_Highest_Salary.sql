SELECT (
    SELECT DISTINCT Salary
    FROM EMployee
    ORDER BY Salary DESC
    LIMIT 1
    OFFSET 1
) AS SecondHighestSalary

# Runtime: 128 ms, faster than 88.31% of MySQL online submissions for Second Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.