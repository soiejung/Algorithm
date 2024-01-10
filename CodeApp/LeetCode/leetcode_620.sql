# Write your MySQL query statement below
# https://leetcode.com/problems/not-boring-movies/description/
select * from cinema
where description != 'boring'
and mod(ID,2) = 1 # 짝수, 홀수 구하는 코드
order by rating desc;
