# Write your MySQL query statement below
# https://leetcode.com/problems/second-highest-salary/

SELECT MAX(salary) as SecondHighestSalary -- output null case 해결(min, avg, max 등 어떠한 집계함수든 상관 없음)
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary desc) AS ranking
    FROM Employee
)A
WHERE ranking = 2
