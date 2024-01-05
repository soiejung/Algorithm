# Write your MySQL query statement below
# https://leetcode.com/problems/employees-with-missing-information/ 

SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Salaries
)

union

SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN(
    SELECT employee_id
    FROM Employees
)
order by employee_id
