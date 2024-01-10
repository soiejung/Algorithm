# Write your MySQL query statement below
# https://leetcode.com/problems/user-activity-for-the-past-30-days-i/ 

SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE DATE_SUB('2019-07-27', INTERVAL 30 DAY) < activity_date
# 특정 날에서 날짜 빼기 cf) DATE_ADD도 있음
AND activity_date < '2019-07-27'
GROUP BY activity_date