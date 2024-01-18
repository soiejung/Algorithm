# Write your MySQL query statement below
# https://leetcode.com/problems/last-person-to-fit-in-the-bus/ 

SELECT person_name
FROM (
    SELECT turn, person_id as ID, person_name, weight, SUM(weight) OVER (ORDER BY turn) as total_weight
    FROM Queue
    ORDER BY turn desc
)A
WHERE total_weight <= 1000
limit 1
