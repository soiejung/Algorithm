# Write your MySQL query statement below
# https://leetcode.com/problems/calculate-special-bonus/ 

SELECT employee_id,
CASE
    WHEN MOD(employee_id,2) = 0 THEN 0
    WHEN MOD(employee_id,2) = 1 AND name NOT LIKE 'M%' THEN salary
    ELSE 0
END AS bonus
FROM Employees
ORDER BY employee_id