
-- patients 테이블 생성
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    birthdate DATE NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(50) UNIQUE,
    address VARCHAR(200),
    PRIMARY KEY (patient_id)
);

-- gender 필드 추가
ALTER TABLE patients
ADD gender VARCHAR(10);

-- phone_number 필드의 데이터 타입 변경
ALTER TABLE patients
MODIFY phone_number VARCHAR(20);

-- patients 테이블의 모든 데이터 삭제
TRUNCATE TABLE patients;