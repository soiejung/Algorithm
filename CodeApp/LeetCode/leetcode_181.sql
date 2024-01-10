# Write your MySQL query statement below
# https://leetcode.com/problems/employees-earning-more-than-their-managers/ 

SELECT E1.name as Employee
FROM Employee E1
WHERE E1.name IN (SELECT E1.name FROM Employee E2 WHERE E1.salary > E2.salary and E1.managerId = E2.id)
