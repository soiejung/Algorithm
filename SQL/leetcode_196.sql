# Write your MySQL query statement below
# https://leetcode.com/problems/delete-duplicate-emails/

DELETE
FROM Person
WHERE id NOT IN (

    SELECT id
    FROM (
        SELECT MIN(p.id) as id
        FROM Person p
        GROUP BY p.email
    )A
)