--change field data type
AlTER TABLE email_subscribers
ALTER COLUMN email SET DATA TYPE varchar(25);

ALTER TABLE bad_orders
ALTER COLUMN quantity SET DATA TYPE int;

ALTER TABLE email_subscribers
ALTER COLUMN frequency SET DATA TYPE smallint;
