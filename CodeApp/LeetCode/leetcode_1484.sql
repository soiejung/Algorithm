# Write your MySQL query statement below
# https://leetcode.com/problems/group-sold-products-by-the-date/ 

SELECT sell_date, COUNT(DISTINCT product) as num_sold, GROUP_CONCAT(DISTINCT product) as products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date