--Add foreign key to existing table

ALTER TABLE practices
DROP CONSTRAINT practices_employeeid_fkey;

ALTER TABLE practices
ADD CONSTRAINT fk_practices_employeeid
FOREIGN KEY (employeeid) REFERENCES employees (employeeid);
