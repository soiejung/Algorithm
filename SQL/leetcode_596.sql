# Write your MySQL query statement below
# https://leetcode.com/problems/classes-more-than-5-students/

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5