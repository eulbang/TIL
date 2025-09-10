
CREATE DATABASE IF NOT EXISTS sns_system_db;

-- 데이터베이스 사용
USE sns_system_db;

-- 사용자 테이블
CREATE TABLE Users (
    user_id INT PRIMARY KEY,  -- 고유한 ID
    name VARCHAR(255),        -- 이름
    email VARCHAR(255)        -- 이메일
);

-- 게시물 테이블
CREATE TABLE Posts (
    post_id INT PRIMARY KEY,  -- 고유한 ID
    title VARCHAR(255),       -- 제목
    content TEXT,             -- 내용
    created_at DATETIME,      -- 작성일
    user_id INT,              -- 작성자 ID (외래 키)
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 댓글 테이블
CREATE TABLE Comments (
    comment_id INT PRIMARY KEY,  -- 고유한 ID
    content TEXT,                -- 내용
    created_at DATETIME,         -- 작성일
    user_id INT,                 -- 작성자 ID (외래 키)
    post_id INT,                 -- 게시물 ID (외래 키)
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (post_id) REFERENCES Posts(post_id)
);