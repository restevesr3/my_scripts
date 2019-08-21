-- DEFAULT CONSTRAINT DEMO

DROP TABLE IF EXISTS practices;
CREATE TABLE practices
(
practice_id int not null PRIMARY KEY,
practice_field varchar(50) NOT NULL,
employeeid INT NOT NULL,
cost int DEFAULT 50 CONSTRAINT practices_cost CHECK(cost >=0 and cost <=1000),
FOREIGN KEY (employeeid) REFERENCES employees (employeeid)

)