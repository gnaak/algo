SELECT 
    B.EMP_NO, 
    B.EMP_NAME, 
    CASE    
        WHEN SUM(C.SCORE) >= 192 THEN 'S'
        WHEN SUM(C.SCORE) >= 180 THEN 'A'
        WHEN SUM(C.SCORE) >= 160 THEN 'B'
        ELSE 'C' 
    END AS GRADE,
    B.SAL * (
        CASE    
            WHEN SUM(C.SCORE) >= 192 THEN 20
            WHEN SUM(C.SCORE) >= 180 THEN 15
            WHEN SUM(C.SCORE) >= 160 THEN 10
            ELSE 0
        END 
    ) / 100 AS BONUS
FROM HR_DEPARTMENT AS A 
JOIN HR_EMPLOYEES AS B 
ON A.DEPT_ID = B.DEPT_ID 
JOIN HR_GRADE AS C 
ON B.EMP_NO = C.EMP_NO
GROUP BY B.EMP_NO
ORDER BY B.EMP_NO