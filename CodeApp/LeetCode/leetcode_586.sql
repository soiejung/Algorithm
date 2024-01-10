# Write your MySQL query statement below
# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/ 

SELECT customer_number
FROM (
    SELECT customer_number, RANK() OVER(ORDER BY cnt desc) AS ranking
    FROM (
        SELECT customer_number, COUNT(order_number) as cnt
        FROM Orders
        GROUP BY customer_number
    )A
)B
WHERE ranking = 1