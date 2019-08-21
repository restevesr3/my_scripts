--Add primary key constraint after table is created

DROP TABLE IF EXISTS practice;

CREATE TABLE practice
(
practice_id INT NOT NULL,
field_name VARCHAR(50) NOT NULL
);

ALTER TABLE practice
ADD PRIMARY KEY (practice_id);

