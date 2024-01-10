# Write your MySQL query statement below
# https://leetcode.com/problems/find-customer-referee/ 

SELECT name
FROM Customer
WHERE id NOT IN (SELECT id FROM Customer WHERE referee_id = '2')
# WHERE referee_id != '2' -> null 값은 포함하지 않는다
