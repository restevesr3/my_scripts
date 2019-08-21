--CREATE ADDITIONAL INDEXES

ALTER TABLE performance_test
ADD COLUMN name text;

UPDATE performance_test
SET name = md5(location)


EXPLAIN ANALYZE SELECT *
FROM
performance_test
WHERE location like 'df%' and name like 'cf%';

create index idx_performance_test_location_name
ON performance_test (location, name);


EXPLAIN ANALYZE SELECT *
FROM performance_test
where location like 'df%'

EXPLAIN ANALYZE SELECT *
FROM performance_test
where name like 'cf%'
