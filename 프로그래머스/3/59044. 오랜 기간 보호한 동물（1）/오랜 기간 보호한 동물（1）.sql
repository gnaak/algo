-- 코드를 입력하세요
SELECT A.NAME, A.DATETIME 
FROM ANIMAL_INS AS A 
LEFT JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID NOT IN (
SELECT ANIMAL_ID FROM ANIMAL_OUTS)
ORDER BY A.DATETIME LIMIT 3