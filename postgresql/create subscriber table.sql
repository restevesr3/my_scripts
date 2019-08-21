--create subscriber table
CREATE TABLE subscriber
(
subscriber_id smallserial NOT NULL PRIMARY KEY,
firstname varchar(50),
lastname varchar(50),
email varchar(50),
sign_up_date timestamp,
frequency integer,
is_customer boolean,
created_date_time timestamp,
created_by varchar(75),
updated_time_stamp timestamp,
updated_by varchar(75)
)