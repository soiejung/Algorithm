# https://school.programmers.co.kr/learn/courses/30/lessons/164673

-- 코드를 입력하세요
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD b
INNER JOIN USED_GOODS_REPLY r
ON b.BOARD_ID = r.BOARD_ID
WHERE DATE_FORMAT(b.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY CREATED_DATE, b.title
