-- 사용자 테이블 생성
CREATE TABLE Users (
    user_id INT PRIMARY KEY,  -- 사용자ID
    name VARCHAR(255),        -- 이름
    email VARCHAR(255)        -- 이메일
);

-- 예시 데이터 삽입
INSERT INTO Users (user_id, name, email) VALUES
(1, '홍길동', 'hong@example.com'),
(2, '이순신', 'lee@example.com');

-- 게시물 테이블 생성
CREATE TABLE Posts (
    post_id INT PRIMARY KEY,  -- 게시물ID
    user_id INT,              -- 사용자ID (외래 키)
    title VARCHAR(255),       -- 제목
    content TEXT,             -- 내용
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 예시 데이터 삽입
INSERT INTO Posts (post_id, user_id, title, content) VALUES
(101, 1, '첫 번째 게시물', '안녕하세요'),
(102, 1, '두 번째 게시물', '반갑습니다'),
(103, 2, '세 번째 게시물', '좋은 하루');

-- 댓글 테이블 생성
CREATE TABLE Comments (
    comment_id INT PRIMARY KEY,  -- 댓글ID
    post_id INT,                 -- 게시물ID (외래 키)
    content TEXT,                -- 내용
    FOREIGN KEY (post_id) REFERENCES Posts(post_id)
);

-- 예시 데이터 삽입
INSERT INTO Comments (comment_id, post_id, content) VALUES
(1001, 101, '첫 댓글'),
(1002, 102, '두 번째 댓글'),
(1003, 103, '세 번째 댓글');

-- 모든 사용자의 이름과 이메일을 조회하는 SQL 쿼리
SELECT name, email
FROM Users;

-- '홍길동' 사용자가 작성한 모든 게시물의 제목과 내용을 조회하는 SQL 쿼리
SELECT title, content
FROM Posts
WHERE user_id = (SELECT user_id FROM Users WHERE name = '홍길동');

-- '첫 번째 게시물'에 달린 모든 댓글의 내용을 조회하는 SQL 쿼리
SELECT content
FROM Comments
WHERE post_id = (SELECT post_id FROM Posts WHERE title = '첫 번째 게시물');

-- 새로운 사용자를 사용자 테이블에 삽입하는 SQL 쿼리
INSERT INTO Users (user_id, name, email) VALUES
(3, '김유신', 'kim@example.com');

-- '이순신' 사용자의 이메일을 'new_lee@example.com'으로 수정하는 SQL 쿼리
UPDATE Users
SET email = 'new_lee@example.com'
WHERE name = '이순신';

