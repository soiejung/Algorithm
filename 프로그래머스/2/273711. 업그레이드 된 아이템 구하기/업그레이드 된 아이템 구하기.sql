SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (
    SELECT t.ITEM_ID
    FROM ITEM_TREE t INNER JOIN ITEM_INFO i
    ON i.ITEM_ID = t.PARENT_ITEM_ID
    WHERE RARITY = 'RARE'
)
ORDER BY ITEM_ID desc