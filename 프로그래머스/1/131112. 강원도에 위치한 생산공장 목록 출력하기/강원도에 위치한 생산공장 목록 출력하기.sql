-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE INSTR(ADDRESS,'강원도') > 0
ORDER bY FACTORY_ID