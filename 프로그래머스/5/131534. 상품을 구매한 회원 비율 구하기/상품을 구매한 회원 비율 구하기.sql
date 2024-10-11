-- 2021년 가입한 회원들 중 
-- 상품을 구매한 회원 수와, 상품을 구매한 회원의 비율 
-- 을 년, 월별로 출력하는 SQL문 
-- 비율은 소수점 둘째자리에서 반올림 
-- 년을 기준으로 오름차순, 월을 기준으로 오름차순 

SELECT 
    YEAR(O.SALES_DATE) AS YEAR, 
    MONTH(O.SALES_DATE) AS MONTH, 
    COUNT(DISTINCT O.USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT O.USER_ID) / (
        SELECT COUNT(DISTINCT USER_ID) 
        FROM USER_INFO
        WHERE JOINED LIKE '2021%'
        )
    ,1) AS PURCHASED_RATIO
FROM USER_INFO AS U 
JOIN ONLINE_SALE AS O 
ON U.USER_ID = O.USER_ID 
WHERE U.JOINED LIKE '2021%'
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH 