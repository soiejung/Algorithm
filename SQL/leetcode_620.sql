# Write your MySQL query statement below

select * from cinema
where description != 'boring'
and mod(ID,2) = 1 # 짝수, 홀수 구하는 코드
order by rating desc;
