# Write your MySQL query statement below
# https://leetcode.com/problems/duplicate-emails/ 

SELECT Email
FROM Person
GROUP BY email
HAVING COUNT(email) >= 2