# Write your MySQL query statement below
# https://leetcode.com/problems/product-sales-analysis-i/description/

SELECT product_name, year, price
FROM Sales INNER JOIN Product
WHERE Sales.product_id = Product.product_id
# on: join 전에 조건을 필터링 / where: join 후에 조건을 필터링
# inner join에서는 상관 없지만 outer join에서 원하는 것을 얻기 위해선 on을 사용해야 함