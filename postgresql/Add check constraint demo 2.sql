--Add check constraint demo 2

ALTER TABLE order_details
ADD CHECK (unitprice >=0);