# Write your MySQL query statement below
# https://leetcode.com/problems/students-and-examinations/

SELECT s.student_id, s.student_name, s.subject_name, IFNULL(attended_exams,0) as attended_exams
FROM
(  
    SELECT student_id, student_name, subject_name
    FROM Students CROSS JOIN Subjects
)s
LEFT OUTER JOIN
(
    SELECT student_id, subject_name, COUNT(student_id) as attended_exams
    FROM Examinations
    GROUP BY subject_name, student_id

)e
ON s.student_id = e.student_id AND s.subject_name = e.subject_name
ORDER BY s.student_id, subject_name
