--CREATE A TABLE demo
CREATE TABLE returns
(
return_id serial not null,
customer_id char(5) not null,
returned_date date,
product_id int,
quantity smallint,
order_id int,
created_time_stamp timestamp,
created_by varchar(75)
)