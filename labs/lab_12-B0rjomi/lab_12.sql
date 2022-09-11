.read fa19_u1337.sql

CREATE TABLE obedience AS
  SELECT seven, instructor 
  FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest 
  FROM students 
  WHERE smallest > 2 
  ORDER BY smallest 
  LIMIT 20 ;

CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color 
  FROM students AS first, students AS second 
  WHERE first.pet = second.pet AND first.song = second.song AND first.time < second.time;

CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM students
  GROUP BY smallest
  HAVING COUNT(*) = 1
  ORDER BY smallest;

CREATE TABLE fa19favpets AS
  SELECT pet, COUNT(*) AS count
  FROM students
  GROUP BY pet
  ORDER BY count DESC, pet DESC LIMIT 10;
  

CREATE TABLE fa19dog AS
  SELECT pet, COUNT(pet)
  FROM students
  WHERE pet = 'собака';

CREATE TABLE obedienceimages AS
  SELECT seven, instructor, COUNT(*) AS count 
  FROM students 
  WHERE seven = '7'
  GROUP BY instructor;