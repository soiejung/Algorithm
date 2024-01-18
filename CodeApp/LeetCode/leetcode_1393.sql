# Write your MySQL query statement below
# https://leetcode.com/problems/capital-gainloss/ 

SELECT stock_name, SUM(
    CASE
        WHEN MOD(rnk,2)= 0 THEN price
        WHEN MOD(rnk,2) = 1 THEN -1 * price
        ELSE 'N/A'
    END
) as capital_gain_loss
FROM (
    SELECT stock_name, operation, DENSE_RANK() OVER(PARTITION BY stock_name ORDER BY operation_day) as rnk, operation_day, price
    FROM Stocks
)A
GROUP BY stock_name