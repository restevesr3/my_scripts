drop table if exists performance_test;
create table performance_test(
id serial,
	location text
);

INSERT INTO performance_test(location)
SELECT md5(random()::text) FROM generate_series(1,10000000);
