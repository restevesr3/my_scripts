--ADD default constraint after table is created

ALTER TABLE orders
ALTER COLUMN shipvia
SET DEFAULT 1;


ALTER TABLE products
ALTER COLUMN reorderlevel
SET DEFAULT 5;