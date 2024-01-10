# Write your MySQL query statement below
# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

SELECT customer_id, COUNT(customer_id) as count_no_trans
FROM (

    SELECT customer_id, v.visit_id as visit_id, transaction_id
    FROM Visits v LEFT OUTER JOIN Transactions t
    ON v.visit_id = t.visit_id
    WHERE transaction_id IS NULL
)A
GROUP BY customer_id

