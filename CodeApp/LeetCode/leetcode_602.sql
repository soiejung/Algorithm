# Write your MySQL query statement below
# https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/ 

SELECT id, COUNT(id) as num
FROM (
    SELECT requester_id as id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id
    FROM RequestAccepted
)A
GROUP BY id
ORDER BY COUNT(id) desc
LIMIT 1