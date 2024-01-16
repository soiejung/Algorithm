# Write your MySQL query statement below
# https://leetcode.com/problems/movie-rating/ 

(
    SELECT u.name as results
    FROM Users u INNER JOIN MovieRating mr
    ON u.user_id = mr.user_id
    GROUP BY mr.user_id
    ORDER BY COUNT(movie_id) desc, u.name
    limit 1
)
UNION ALL
(
    SELECT m.title as results
    FROM Movies m
    INNER JOIN (

        SELECT movie_id, AVG(rating) as average
        FROM MovieRating
        WHERE DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
        GROUP BY movie_id
    )mr
    ON m.movie_id = mr.movie_id
    ORDER BY average desc, m.title
    limit 1
)

