# Write your MySQL query statement below
# https://leetcode.com/problems/article-views-i/description/
select Distinct author_id as id from Views
where author_id = viewer_id
order by author_id