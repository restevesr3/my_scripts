--Add check constraint after table creation

ALTER TABLE ORDERS
ADD CONSTRAINT ck_orders_freight CHECK (freight > 0);