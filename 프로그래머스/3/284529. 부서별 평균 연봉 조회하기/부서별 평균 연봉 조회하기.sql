-- 코드를 작성해주세요 부서별 평균 연봉 구하기 
-- 부서별로 부서 ID, 영문 부서명, 평균 연봉 조회 

SELECT A.DEPT_ID, A.DEPT_NAME_EN, ROUND(AVG(B.SAL),0) AS AVG_SAL
FROM HR_DEPARTMENT AS A 
JOIN HR_EMPLOYEES AS B 
ON A.DEPT_ID = B.DEPT_ID
GROUP BY A.DEPT_ID
ORDER BY AVG_SAL DESC


