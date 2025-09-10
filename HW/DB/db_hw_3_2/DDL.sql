DROP DATABASE IF EXISTS library_db;
CREATE DATABASE library_db;
USE library_db;

CREATE TABLE authors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL);
CREATE TABLE genres  (id INT AUTO_INCREMENT PRIMARY KEY, genre_name VARCHAR(100) NOT NULL);

INSERT INTO authors (name) VALUES
('J.K. Rowling'), ('George R.R. Martin'), ('J.R.R. Tolkien'), ('Isaac Asimov'), ('Agatha Christie');

INSERT INTO genres (genre_name) VALUES
('Fantasy'), ('Science Fiction'), ('Mystery'), ('Thriller');

CREATE TABLE books (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  author_id INT REFERENCES authors(id),
  genre_id  INT REFERENCES genres(id)
);

INSERT INTO books (title, author_id, genre_id)
SELECT t.title, a.id, g.id
FROM (
  SELECT 'Harry Potter and the Philosopher''s Stone' AS title, 'J.K. Rowling' AS an, 'Fantasy' AS gn UNION ALL
  SELECT 'Harry Potter and the Chamber of Secrets' , 'J.K. Rowling'        , 'Fantasy'         UNION ALL
  SELECT 'A Game of Thrones'                       , 'George R.R. Martin'  , 'Fantasy'         UNION ALL
  SELECT 'A Clash of Kings'                        , 'George R.R. Martin'  , 'Fantasy'         UNION ALL
  SELECT 'The Hobbit'                              , 'J.R.R. Tolkien'      , 'Fantasy'         UNION ALL
  SELECT 'The Lord of the Rings'                   , 'J.R.R. Tolkien'      , 'Fantasy'         UNION ALL
  SELECT 'Foundation'                              , 'Isaac Asimov'        , 'Science Fiction' UNION ALL
  SELECT 'I, Robot'                                , 'Isaac Asimov'        , 'Science Fiction' UNION ALL
  SELECT 'Murder on the Orient Express'            , 'Agatha Christie'     , 'Mystery'         UNION ALL
  SELECT 'The Mysterious Affair at Styles'         , 'Agatha Christie'     , 'Mystery'         UNION ALL
  SELECT 'The Girl with the Dragon Tattoo'         , 'Agatha Christie'     , 'Thriller'
) t
JOIN authors a ON a.name = t.an
JOIN genres  g ON g.genre_name = t.gn;

SELECT b.id, b.title, a.name AS author, g.genre_name AS genre
FROM books b JOIN authors a ON b.author_id=a.id JOIN genres g ON b.genre_id=g.id
ORDER BY b.id;
