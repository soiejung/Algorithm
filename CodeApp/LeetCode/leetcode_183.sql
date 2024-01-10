# Write your MySQL query statement below
# https://leetcode.com/problems/customers-who-never-order/ 

SELECT c.name as Customers
FROM Customers c
WHERE c.id NOT IN (SELECT o.customerId FROM Orders o)