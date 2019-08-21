--Add foreign key at table creation part 2
DROP TABLE IF EXISTS pets;
CREATE TABLE pets
(
pet_id int primary key,
pet_name varchar(25) NOT NULL,
customerid CHAR(5),
FOREIGN KEY (customerid) REFERENCES customers (customerid)
);

