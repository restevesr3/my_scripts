--REMOVE A DEFAULT VALUE

ALTER TABLE PRODUCTS
ALTER COLUMN reorderlevel DROP DEFAULT;

ALTER TABLE suppliers
ALTER COLUMN homepage SET DEFAULT 'NOT AVAILABLE';

ALTER TABLE suppliers
ALTER COLUMN homepage DROP DEFAULT;