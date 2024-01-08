# Write your MySQL query statement below
# https://leetcode.com/problems/biggest-single-number/ 

SELECT max(n.num) as num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING IFNULL(COUNT(num) = 1,null)
)n