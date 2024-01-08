# Write your MySQL query statement below
# https://leetcode.com/problems/find-total-time-spent-by-each-employee/ 

SELECT event_day as day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY emp_id, event_day