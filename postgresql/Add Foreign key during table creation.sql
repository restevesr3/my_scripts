--Add Foreign key during table creation

DROP TABLE IF EXISTS practices;
CREATE TABLE practices
(
practiceid INT primary key,
practicefield varchar(50) NOT NULL,
employeeid int NOT NULL,
FOREIGN KEY (employeeid) REFERENCES employees (employeeid));