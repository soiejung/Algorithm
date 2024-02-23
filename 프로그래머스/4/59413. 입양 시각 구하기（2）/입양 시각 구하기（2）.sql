-- 코드를 입력하세요
with RECURSIVE HOURS AS (
    SELECT 0 AS HOUR # 초기 값 설정
    
    UNION ALL # RECURSIVE 사용 시 필수. 다음에 이어붙어야 할 때 사용
    
    SELECT HOUR + 1 FROM HOURS
    WHERE HOUR < 23 # RECURSIVE 사용 시 필수. 정지 조건 필요할 때 사용

), ANIMAL_OUTS_HOUR AS (
    SELECT DATE_FORMAT(DATETIME,'%H') AS HOUR,COUNT(ANIMAL_ID) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
    ORDER BY HOUR
)

SELECT h.HOUR, IFNULL(COUNT, 0) AS COUNT
FROM HOURS h LEFT OUTER JOIN ANIMAL_OUTS_HOUR a
ON h.HOUR = a.HOUR