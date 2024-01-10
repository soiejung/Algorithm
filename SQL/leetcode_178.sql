# Write your MySQL query statement below
# https://leetcode.com/problems/rank-scores/ 

SELECT score, DENSE_RANK() OVER (ORDER BY score desc) as 'rank'
FROM Scores