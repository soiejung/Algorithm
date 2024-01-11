# Write your MySQL query statement below
# https://leetcode.com/problems/market-analysis-i/ 

SELECT A.user_id as buyer_id, join_date, IFNULL(cnt,0) as orders_in_2019
FROM
(
    SELECT DISTINCT user_id, join_date
    FROM  Users
)A
LEFT OUTER JOIN
(
    SELECT buyer_id, COUNT(buyer_id) as cnt
    FROM Orders o
    WHERE EXTRACT(YEAR FROM order_date) = '2019'
    GROUP BY buyer_id
)B
ON A.user_id = B.buyer_id