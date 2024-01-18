# Write your MySQL query statement below
# https://leetcode.com/problems/immediate-food-delivery-ii/ 

SELECT ROUND(SUM(
    CASE
        WHEN order_date = customer_pref_delivery_date THEN 1
        ELSE 0
    END
)/COUNT(*)*100,2) as immediate_percentage
FROM (
    SELECT customer_id, order_date, customer_pref_delivery_date, RANK() OVER (PARTITION BY customer_id ORDER BY order_date) as rnk
    FROM Delivery
)A
WHERE rnk = 1