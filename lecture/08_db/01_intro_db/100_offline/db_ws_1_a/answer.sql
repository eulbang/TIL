-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS restaurant_db;

-- 데이터베이스 사용
USE restaurant_db;

-- restaurants 테이블 생성
CREATE TABLE IF NOT EXISTS restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    cuisine_type VARCHAR(100)
);

-- menus 테이블 생성
CREATE TABLE IF NOT EXISTS menus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT,
    item_name VARCHAR(255),
    price DECIMAL(10, 2),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);