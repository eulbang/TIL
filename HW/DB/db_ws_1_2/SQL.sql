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

CREATE TABLE hospital (
  hospital_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  location VARCHAR(200) NOT NULL,
  established_date TIMESTAMP,
  contact_number VARCHAR(20) UNIQUE,
  type VARCHAR(50) NOT NULL
)

ALTER TABLE hospital
ADD COLUMN capacity INT;

ALTER TABLE hospital
MODIFY COLUMN type VARCHAR(100);

ALTER TABLE hospital
RENAME COLUMN established_date TO founded_date;

DROP TABLE hospital;