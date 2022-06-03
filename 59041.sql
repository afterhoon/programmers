-- 동명 동물 수 찾기
-- https://programmers.co.kr/learn/courses/30/lessons/59041

SELECT NAME, COUNT(*) 
FROM ANIMAL_INS 
WHERE NOT NAME IS NULL 
GROUP BY NAME 
HAVING COUNT(*) > 1 
ORDER BY NAME;