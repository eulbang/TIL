-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS hospital_db;

-- 데이터베이스 사용
USE hospital_db;

-- hospital 테이블 생성
CREATE TABLE hospital (
    hospital_id INT AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    location VARCHAR(200) NOT NULL,
    established_date DATE,
    contact_number VARCHAR(20) UNIQUE,
    type VARCHAR(50) NOT NULL,
    PRIMARY KEY (hospital_id)
);

-- capacity 필드 추가
ALTER TABLE hospital
ADD capacity INT;

-- type 필드의 데이터 타입 변경
ALTER TABLE hospital
MODIFY type VARCHAR(100);

-- established_date 필드의 이름 변경
ALTER TABLE hospital
CHANGE established_date founded_date DATE;

-- hospital 테이블 삭제
DROP TABLE hospital;