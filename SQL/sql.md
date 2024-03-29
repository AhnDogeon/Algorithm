# 여기에 SQL 문제 정리



#### 없어진동물 찾기

```mysql
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
LEFT OUTER JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID is NULL
ORDER BY OUTS.ANIMAL_ID
```

#### 없어진 기록 찾기

```mysql
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME FROM ANIMAL_OUTS
LEFT OUTER JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_INS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_OUTS.ANIMAL_ID
```

#### 있었는데요 없었습니다

```mysql
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM ANIMAL_INS
LEFT JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME
```

#### 오랜기간 보호한 동물(1)

```mysql
SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME 
FROM ANIMAL_INS
LEFT OUTER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_OUTS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_INS.DATETIME LIMIT 3
```

#### 보호소에서 중성화한 동물

```mysql
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.ANIMAL_TYPE, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
LEFT JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_INS.SEX_UPON_INTAKE LIKE 'Intact%'
AND (ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%' OR ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%')
```

#### 이름이 없는 동물의 아이디

```mysql
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NULL
```

#### 이름이 있는 동물의 아이디

```mysql
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NOT NULL
```

#### NULL 처리하기

```mysql
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
```

#### 고양이와 개는 몇 마리 있을까

```mysql
SELECT ANIMAL_TYPE, COUNT(*) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE
```

#### 루시와 엘라 찾기

```mysql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME = "Lucy" OR NAME="Ella" OR NAME="Pickle" OR NAME="Rogan" OR NAME = "Sabrina" OR NAME = "Mitty"
```

#### 동명 동물 수 찾기

```mysql
SELECT NAME, COUNT(*) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >= 2
```

#### 이름에 el이 들어가는 동물 찾기

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'DOG'
ORDER BY NAME
```

#### 입양 시각 구하기(1)

```mysql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME)AS COUNT 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19 
GROUP BY HOUR
```

#### 상위 n개 레코드

```mysql
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
```

#### 모든 레코드 조회하기

```mysql
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID
```

#### 역순 정렬하기

```mysql
SELECT NAME, DATETIME FROM ANIMAl_INS ORDER BY ANIMAL_ID DESC
```

#### 서브쿼리

```mysql
SELECT STUDNO, NAME, BIRDTHDATE 
FROM STUDENT
WHERE BIRTHDATE = (
SELECT MIN(BIRTHDATE)
FROM STUDENT)
```
