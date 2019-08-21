-- Create table with unique contraint

DROP TABLE IF EXISTS pets;
CREATE TABLE pets
(
pet_id int not null unique,
pet_name varchar(25) not null
);
