--Add Parallelization Back

SET max_parallel_workers_per_gather = 4;

EXPLAIN (ANALYZE, VERBOSE) SELECT * FROM performance_test
WHERE location like 'ab%'