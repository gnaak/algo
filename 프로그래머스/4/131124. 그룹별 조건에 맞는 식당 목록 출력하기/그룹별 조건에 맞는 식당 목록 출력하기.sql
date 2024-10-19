-- 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성 

SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE 
FROM MEMBER_PROFILE AS A 
JOIN REST_REVIEW AS B 
ON A.MEMBER_ID = B.MEMBER_ID
JOIN(
    SELECT MEMBER_ID FROM REST_REVIEW 
    GROUP BY MEMBER_ID 
    ORDER BY COUNT(*) DESC 
    LIMIT 1
)AS LIM
ON A.MEMBER_ID = LIM.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT