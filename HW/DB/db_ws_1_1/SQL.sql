CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE patients (
  patient_id INT PRIMARY KEY AUTO_INCREMENT,
  name CHAR(100) NOT NULL,
  birth_date TIMESTAMP NOT NULL,
  phone_number CHAR(15),
  email CHAR(50) UNIQUE,
  address CHAR(200)
)

ALTER TABLE patients
ADD COLUMN gender VARCHAR(10);

ALTER TABLE patients
MODIFY COLUMN phone_number VARCHAR(20);