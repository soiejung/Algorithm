-- 코드를 작성해주세요
SELECT QUARTER, COUNT(ID) AS ECOLI_COUNT
FROM (
    SELECT ID, CASE 
        WHEN EXTRACT(MONTH FROM DIFFERENTIATION_DATE) >= 1 AND EXTRACT(MONTH FROM DIFFERENTIATION_DATE) <= 3 THEN '1Q'
        WHEN EXTRACT(MONTH FROM DIFFERENTIATION_DATE) >= 4 AND EXTRACT(MONTH FROM DIFFERENTIATION_DATE) <= 6 THEN '2Q'WHEN EXTRACT(MONTH FROM DIFFERENTIATION_DATE) >= 7 AND EXTRACT(MONTH FROM DIFFERENTIATION_DATE) <= 9 THEN '3Q'WHEN EXTRACT(MONTH FROM DIFFERENTIATION_DATE) >= 10 AND EXTRACT(MONTH FROM DIFFERENTIATION_DATE) <= 12 THEN '4Q'
        END AS QUARTER
    FROM ECOLI_DATA
)A
GROUP BY QUARTER
ORDER BY QUARTER