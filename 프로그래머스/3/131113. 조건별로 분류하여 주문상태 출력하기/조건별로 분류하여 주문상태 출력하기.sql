-- 2022년 5월 1일을 기준으로 주문ID, 제품ID, 출고일자, 출고여부를 조회하는 SQL
-- 2022년 5월 1일까지 출과완료로 이후 날짜는 출고 대기로 미정이면 출고미정으로 
-- 결과는 주문ID를 기준으로 오름차순 
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE, 
    CASE 
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
        ELSE '출고미정'
        END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID