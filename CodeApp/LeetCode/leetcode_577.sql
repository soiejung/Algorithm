# Write your MySQL query statement below
# https://leetcode.com/problems/employee-bonus/ 

SELECT name, bonus
FROM
(
    SELECT empId, name
    FROM Employee
    WHERE empId NOT IN (
        SELECT empId 
        FROM Bonus
        WHERE bonus >= 1000
        )
) e
LEFT OUTER JOIN Bonus b
ON e.empId = b.empId

