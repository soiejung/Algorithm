-- 코드를 입력하세요
SELECT DISTINCT h.CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h INNER JOIN CAR_RENTAL_COMPANY_CAR c
ON h.CAR_ID = c.CAR_ID
WHERE CAR_TYPE = '세단' and START_DATE >= '2022-10-01'
ORDER BY CAR_ID desc