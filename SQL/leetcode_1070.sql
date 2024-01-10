# Write your MySQL query statement below
# https://leetcode.com/problems/product-sales-analysis-iii/ 

SELECT product_id, year as first_year, quantity, price
FROM (
    SELECT product_id, year, quantity, price, rank() OVER(PARTITION BY product_id ORDER BY year) as ranking
    FROM Sales
)A
WHERE ranking = 1