# Write your MySQL query statement below
# https://leetcode.com/problems/the-latest-login-in-2020 

SELECT user_id, MAX(time_stamp) as last_stamp
FROM Logins
WHERE time_stamp NOT IN (
    SELECT time_stamp
    FROM Logins
    WHERE EXTRACT(YEAR FROM time_stamp) != '2020'
)
GROUP BY user_id
