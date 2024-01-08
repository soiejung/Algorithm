# Write your MySQL query statement below
# https://leetcode.com/problems/top-travellers/ 

SELECT name, IFNULL(SUM(distance),0) as travelled_distance
FROM Users u LEFT OUTER JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance desc,name