# Write your MySQL query statement below
# https://leetcode.com/problems/bank-account-summary-ii/ 

SELECT name, SUM(amount) as balance
FROM Users u INNER JOIN Transactions t
ON u.account = t.account
GROUP BY u.account
HAVING balance > 10000