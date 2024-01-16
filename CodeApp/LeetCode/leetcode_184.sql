# Write your MySQL query statement below
# https://leetcode.com/problems/department-highest-salary/ 

SELECT Department, e.name as Employee, Salary
FROM Employee e
INNER JOIN (

    SELECT d.id as id, d.name as Department, MAX(Salary) as max_salary
    FROM Employee e INNER JOIN Department d
    ON e.departmentId = d.id
    GROUP BY e.departmentId
) A
ON e.departmentId = A.id
WHERE e.salary = A.max_salary