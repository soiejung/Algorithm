# Write your MySQL query statement below
# https://leetcode.com/problems/average-time-of-process-per-machine/ 

SELECT machine_id, ROUND(AVG(processing_time),3) as processing_time
FROM (
    SELECT machine_id, SUM(processing_time) as processing_time
    FROM (
        SELECT machine_id, process_id,
        CASE 
            WHEN activity_type = 'start' THEN -1*timestamp
            WHEN activity_type = 'end' THEN timestamp
            ELSE 'N/A'
        END AS processing_time
        FROM Activity
    )A
    GROUP BY machine_id, process_id
)B
GROUP BY machine_id