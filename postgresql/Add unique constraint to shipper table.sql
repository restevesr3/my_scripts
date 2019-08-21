-- Add unique constraint to shipper table

SELECT * FROM shippers;

ALTER TABLE shippers
ADD CONSTRAINT uq_shipper_companyname UNIQUE (companyname);
