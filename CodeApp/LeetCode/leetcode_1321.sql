# Write your MySQL query statement below
# https://leetcode.com/problems/restaurant-growth/ 

SELECT 
a.visited_on, 
(
    SELECT SUM(amount)
    FROM Customer c
    WHERE DATEDIFF(a.visited_on,c.visited_on) BETWEEN 0 and 6
) as amount,
ROUND(
(
    SELECT SUM(b.amount)/7 as sum_amount
    FROM Customer b
    WHERE DATEDIFF(a.visited_on, b.visited_on) BETWEEN 0 AND 6
),2
) as average_amount
FROM Customer a
WHERE DATEDIFF(a.visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6
GROUP BY a.visited_on
ORDER BY a.visited_on