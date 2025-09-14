DROP DATABASE sns_system_4;
CREATE DATABASE sns_system_4;
USE sns_system_4;

CREATE TABLE user_data (
  user_id INT,
  username VARCHAR(50),
  email VARCHAR(100),
  post_id INT,
  title VARCHAR(200),
  content TEXT,
  comment_id INT,
  comment_content TEXT
);

INSERT INTO user_data (user_id, username, email, post_id, title, content, comment_id, comment_content)
VALUES
(1, '홍길동', 'hong@example.com', 101, '첫 번째 게시물', '안녕하세요', 1001, '첫 댓글'),
(1, '홍길동', 'hong@example.com', 102, '두 번쨰 게시물', '반갑습니다', 1002, '두 번째 댓글'),
(2, '이순신', 'lee@example.com', 103, '세 번째 게시물', '좋은 하루', 1003, '세 번째 댓글');

ALTER TABLE user_data
MODIFY user_id INT NOT NULL,
MODIFY post_id INT NOT NULL,
MODIFY comment_id INT NOT NULL;

ALTER TABLE user_data
ADD PRIMARY KEY (user_id, post_id, comment_id);

CREATE TABLE users (
  user_id INT PRIMARY KEY,
  username VARCHAR(50),
  email VARCHAR(100)
)

CREATE TABLE posts (
  post_id INT PRIMARY KEY,
  user_id INT NOT NULL,
  title   VARCHAR(200),
  content TEXT,
  CONSTRAINT fk_posts_user
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE CASCADE ON UPDATE CASCADE
)

CREATE TABLE comments (
  comment_id INT PRIMARY KEY,
  post_id    INT NOT NULL,
  user_id    INT NOT NULL,
  content    TEXT,
  CONSTRAINT fk_comments_post
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_comments_user
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE CASCADE ON UPDATE CASCADE
)

INSERT INTO users (user_id, username, email)
SELECT DISTINCT user_id, username, email
FROM user_data;

INSERT INTO posts (post_id, user_id, title, content)
SELECT DISTINCT post_id, user_id, title, content
FROM user_data;

INSERT INTO comments (comment_id, post_id, user_id, content)
SELECT DISTINCT comment_id, post_id, user_id, comment_content
FROM user_data;