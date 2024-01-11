# https://leetcode.com/problems/product-price-at-a-given-date/
SELECT P.product_id, IFNULL(PP.new_price,10) as price
FROM
(
    SELECT DISTINCT product_id
    FROM Products
)P
LEFT OUTER JOIN
(
    SELECT product_id, new_price
    FROM(
        SELECT product_id, new_price, change_date, RANK() OVER(PARTITION BY product_id ORDER BY change_date desc) AS rnk
        FROM Products
        WHERE change_date <= '2019-08-16'
    )B
    WHERE rnk = 1
)PP
ON P.product_id =PP.product_id