SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS AS A
RIGHT JOIN ANIMAL_OUTS AS B
USING (ANIMAL_ID)
WHERE A.SEX_UPON_INTAKE NOT LIKE B.SEX_UPON_OUTCOME