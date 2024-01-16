# Write your MySQL query statement below
# https://leetcode.com/problems/game-play-analysis-iv/ 
# prev_id, prev_date 수정 (ORDER BY에 event_date 추가)
SELECT ROUND(COUNT(player_id) /(SELECT COUNT(DISTINCT player_id) FROM Activity),2) as fraction
FROM 
(
    SELECT player_id, 
        event_date,
        RANK() OVER (PARTITION BY player_id ORDER bY event_date) AS rnk,
        LAG(player_id) OVER (ORDER BY player_id, event_date) AS prev_id,
        LAG(event_date) OVER (ORDER BY player_id, event_date) AS prev_date
    FROM Activity
) A
WHERE rnk = 2
AND DATE_ADD(prev_date, INTERVAL 1 day) = event_date AND player_id = prev_id
