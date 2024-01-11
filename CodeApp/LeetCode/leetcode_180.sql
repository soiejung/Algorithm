# Write your MySQL query statement below
# https://leetcode.com/problems/consecutive-numbers/

SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT id, num, LEAD(num) OVER(ORDER BY id) as n1, LEAD(num, 2) OVER (ORDER BY id) as n2
    FROM Logs
)A
WHERE num = n1 AND n1 = n2 AND n2 = num