-- Add Unique constraint to column demo

DROP TABLE IF EXISTS practices;
CREATE TABLE practices
(
practiceid int UNIQUE,
practice_field VARCHAR(50) NOT NULL
)