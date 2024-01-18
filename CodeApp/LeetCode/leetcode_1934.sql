# Write your MySQL query statement below
# https://leetcode.com/problems/confirmation-rate/ 

SELECT s.user_id, ROUND(IFNULL(confirmation_rate,0),2) as confirmation_rate
FROM Signups s
LEFT OUTER JOIN
(
    SELECT user_id, 
    SUM(
        CASE
            WHEN action = "confirmed" THEN 1
            ELSE 0
        END
    )/COUNT(action) as confirmation_rate
    FROM Confirmations
    GROUP BY user_id
)A
ON s.user_id = A.user_id