-- 코드를 입력하세요
SELECT A.PRODUCT_ID, A.PRODUCT_NAME, SUM(B.AMOUNT*A.PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT AS A 
JOIN FOOD_ORDER AS B 
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE B.PRODUCE_DATE LIKE '%22-05%'
GROUP BY B.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID