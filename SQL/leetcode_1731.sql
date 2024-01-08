# Write your MySQL query statement below
# https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/ 

SELECT employee_id, name, COUNT(mannager_id) as reports_count,ROUND(AVG(mannager_age),0) as average_age
FROM (
    SELECT e1.employee_id as employee_id, e1.name as name, e2.employee_id as mannager_id, e2.age as mannager_age
    FROM Employees e1 INNER JOIN Employees e2
    ON e1.employee_id = e2.reports_to
)e
GROUP BY employee_id
ORDER BY employee_id