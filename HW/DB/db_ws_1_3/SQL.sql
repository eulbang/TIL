CREATE DATABASE sns_system_db;
USE sns_system_db;

CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  email VARCHAR(100)
);

CREATE TABLE posts (
  post_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  title VARCHAR(100),
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE comments (
  comment_id INT AUTO_INCREMENT PRIMARY KEY,
  post_id INT,
  user_id INT,
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (post_id) REFERENCES posts(post_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);
ALTER TABLE posts
  ADD CONSTRAINT fk_posts_user
  FOREIGN KEY (user_id) REFERENCES users(user_id);

ALTER TABLE comments
  ADD CONSTRAINT fk_comments_post
  FOREIGN KEY (post_id) REFERENCES posts(post_id),
  ADD CONSTRAINT fk_comments_user
  FOREIGN KEY (user_id) REFERENCES users(user_id);