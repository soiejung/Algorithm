# Write your MySQL query statement below
# https://leetcode.com/problems/exchange-seats/ 

SELECT id, 
IFNULL(
    CASE
        WHEN MOD(id,2) = 0 THEN swap1
        WHEN MOD(id,2) = 1 THEN swap2
        ELSE 'N/A'
    END,student) AS student
FROM (
    SELECT id, student, LAG(student) OVER(ORDER BY id) as swap1, LEAD(student) OVER(ORDER BY id) as swap2
    FROM Seat
)A