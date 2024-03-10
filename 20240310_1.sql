-- programmers sql select ps
-- 재구매가 일어난 상품과 회원 리스트 구하기

SELECT USER_ID,	PRODUCT_ID
FROM ONLINE_SALE 
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(USER_ID) > 1  -- HAVING: 결과값 필터링, COUNT(PRODUCT_ID)해도 무방함
ORDER BY USER_ID, PRODUCT_ID DESC