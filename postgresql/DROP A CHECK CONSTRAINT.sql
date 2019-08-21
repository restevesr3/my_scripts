--DROP A CHECK CONSTRAINT
--To solve this problem script the table
--to get the constraint name

ALTER TABLE products
DROP CONSTRAINT products_reorderlevel_check;
