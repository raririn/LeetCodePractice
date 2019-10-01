# Write your MySQL query statement below
SELECT Customers.Name AS Customers
FROM Customers
WHERE (
    Customers.ID NOT IN (
        SELECT Orders.CustomerID
        FROM Orders
    )
)

# Runtime: 233 ms, faster than 84.41% of MySQL online submissions for Customers Who Never Order.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.