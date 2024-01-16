# Write your MySQL query statement below
# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/ 

SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(id) >= 5
)