--Create a check constraint demo
DROP TABLE IF EXISTS practices;
CREATE TABLE practices
(
practice_id int not null primary key,
practicefield VARCHAR(50) NOT NULL,
employeeid int NOT NULL,
dollar_cost int CONSTRAINT ck_practices_dollar_cost CHECK (dollar_cost >=0 and dollar_cost <=100),
FOREIGN KEY (employeeid) REFERENCES employees (employeeid)
);

INSERT INTO practices
(practiceid, practicefield, employeeid, dollar_cost)
VALUES
(1, 'some_name', 1, 1500);