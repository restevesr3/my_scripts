--CREATE PRIMARY KEY DEMO

DROP TABLE IF EXISTS practice;
CREATE TABLE practice
(
practice_id int primary key,
field_name_1 varchar(50) NOT NULL
);


DROP TABLE IF EXISTS pets;
CREATE TABLE pets
(
pet_id int primary key,
pet_name varchar(50)
);