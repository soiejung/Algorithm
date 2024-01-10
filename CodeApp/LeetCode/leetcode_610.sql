# Write your MySQL query statement below
# https://leetcode.com/problems/triangle-judgement/ 

SELECT x, y, z, 
CASE

    WHEN x + y > z and y + z > x and z + x > y then 'Yes'
    ELSE 'No'

END AS triangle
FROM Triangle