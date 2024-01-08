# Write your MySQL query statement below
# https://leetcode.com/problems/rising-temperature/ 

SELECT id
FROM (
    SELECT id, recordDate,temperature,
    LAG(recordDate) OVER (ORDER BY recordDate) as prev_date,
    LAG(temperature) OVER(ORDER BY recordDate) AS prev_temperature
    FROM Weather
)A
WHERE temperature > prev_temperature
AND DATE_ADD(prev_date, INTERVAL 1 day) = recordDate