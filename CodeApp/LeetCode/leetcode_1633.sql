# Write your MySQL query statement below
# https://leetcode.com/problems/percentage-of-users-attended-a-contest/ 

SELECT contest_id, ROUND(cnt/total*100,2) as percentage
FROM (

    SELECT contest_id, COUNT(user_id) as cnt
    FROM Register
    GROUP BY contest_id
)a,
(
    SELECT COUNT(user_id) as total
    FROM Users
)b
GROUP BY contest_id
ORDER BY percentage desc, contest_id