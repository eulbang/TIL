CREATE DATABASE movies;
USE movies;
CREATE TABLE movie_list (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255),
  genre VARCHAR(100),
  release_year YEAR
);
INSERT INTO movie_list (title, genre, release_year)
VALUES 
  ('Inception', 'Sci-Fi', 2010),
  ('The Dark Knight', 'Action', 2008),
  ('Interstellar', 'Sci-Fi', 2014),
  ('Unknown', 'Drama', Null),
  ('The Shawshank Redemption', 'Drama', 1994),
  ('Fight Club', 'Drama', 1999),
  ('Mad Max: Fury Road', 'Action', 2015),
  ('Star Wars: The Force Awakens', 'Sci-Fi', 2015);

SELECT *
FROM movie_list
WHERE release_year > 2010;

SELECT *
FROM movie_list
WHERE genre = 'Action' OR genre = 'Sci-Fi';

SELECT *
FROM movie_list
WHERE title LIKE '%The%';

SELECT *
FROM movie_list
WHERE release_year >= 2008 AND release_year <=2014;

SELECT *
FROM movie_list
WHERE release_year IS NULL;

SELECT *
FROM movie_list
WHERE release_year >= 2000 AND release_year <= 2010;

SELECT *
FROM movie_list
WHERE LEFT(title, 1) BETWEEN 'A' AND 'L';

SELECT *
FROM movie_list
WHERE genre = 'Drama' AND release_year >= 1990 AND release_year <= 2000;

SELECT *
FROM movie_list
WHERE release_year BETWEEN 2015 AND 2020 AND genre IN ('Sci-Fi', 'Action');

SELECT *
FROM movie_list
WHERE release_year > 2005 AND release_year < 2015;

INSERT INTO movie_list (title, genre, release_year)
VALUES
  ('The Matrix', 'Sci-Fi', 1999),
  ('Gladiator', 'Action', 2000),
  ('Jurassic Park', 'Sci-Fi', 1993),
  ('The Fugitive', 'Action', 1993);

SELECT title
FROM movie_list
WHERE genre = 'Drama'
  AND release_year = (
    SELECT MIN(release_year)
    FROM movie_list
    WHERE genre = 'Drama'
  )

SELECT title, release_year
FROM movie_list
WHERE genre = 'Action'
  AND release_year = (
    SELECT MAX(release_year)
    FROM movie_list
    WHERE genre = 'Action' AND release_year > 2000
  );

SELECT *
FROM movie_list
WHERE genre in ('Sci-Fi', 'Action') AND release_year IN (
  SELECT release_year
  FROM movie_list
  WHERE genre = 'Drama'
);

SELECT *
FROM movie_list
WHERE genre = 'Sci-Fi' AND release_year > (
  SELECT AVG(release_year)
  FROM movie_list
  WHERE genre = 'Action'
);

SELECT *
FROM movie_list
WHERE genre NOT IN ('Action') AND release_year = (
  SELECT MIN(release_year)
  FROM movie_list
  WHERE genre = 'Action'
);