# Write your MySQL query statement below
# https://leetcode.com/problems/list-the-products-ordered-in-a-period/ 

SELECT product_name, unit
FROM Products p
INNER JOIN
(
    SELECT product_id, SUM(unit) as unit
    FROM Orders
    WHERE EXTRACT(YEAR_MONTH FROM order_date) = '202002'
    GROUP BY product_id
    HAVING SUM(unit)>=100
) o 
WHERE p.product_id = o.product_id