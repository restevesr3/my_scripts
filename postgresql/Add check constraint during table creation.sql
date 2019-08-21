-- Add check constraint during table creation

DROP TABLE IF EXISTS pets;
CREATE TABLE pets
(
pet_id int not null primary key,
pet_name varchar(25) not null,
customerid CHAR(5) NOT NULL,
pet_weight NUMERIC(5,2) CONSTRAINT ck_pet_pet_weight CHECK (pet_weight > 0 and pet_weight < 200),
FOREIGN KEY (customerid) REFERENCES customers (customerid)
);

INSERT INTO pets
(pet_id, pet_name, customerid, pet_weight)
VALUES
()