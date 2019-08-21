
--DEFAULT CONSTRAINT demo part 2

DROP TABLE IF EXISTS pets;
CREATE TABLE pets
(
pet_id int not null primary key,
pet_name varchar(25) not null,
customerid char(5) not null,
weight int DEFAULT 5 CONSTRAINT ck_pets_weight CHECK (weight >0 and weight <200),
FOREIGN KEY (customerid) REFERENCES customers(customerid)	

)