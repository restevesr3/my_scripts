--using the gin_trgm_ops index
EXPLAIN ANALYZE SELECT
location
FROM
performance_test
WHERE name LIKE '%dfe%';


EXPLAIN ANALYZE SELECT location
FROM
performance_test
WHERE
location LIKE '%dfe%'