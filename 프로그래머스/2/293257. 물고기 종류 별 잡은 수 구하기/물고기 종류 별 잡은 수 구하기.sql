-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT, FISH_NAME
FROM FISH_INFO i INNER JOIN FISH_NAME_INFO n
ON i.FISH_TYPE = n.FISH_TYPE
GROUP BY FISH_NAME
ORDER BY FISH_COUNT DESC