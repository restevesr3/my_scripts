--Set parellization to 1 cpu
SET max_parallel_workers_per_gather = 0;

-- run query on field without index
EXPLAIN SELECT *
FROM performance_test
WHERE location like 'ab%';

/* 2 BASIC TYPES OF COSTS
1. I/O Costs - reading and writing to disk
2. CPU Costs - processing data
Here is the formula:
Number of relation pages * seq_page_cost + Number of rows * cpu_tuple_cost + Number of rows * cpu_operator_cost

WHAT ARE RELATION PAGES
Every table and index is stored as an array of pages of fixed size (default 8KB).
So for a table the relation pages are 8KB chunks of data.

HOW TO SEE TABLE SIZE

SELECT 
pg_relation_size('performance_test'),
pg_size_pretty(pg_relation_size('performance_test'))

WHERE TO FIND RELATION PAGES
select 
relpages
FROM
pg_class
WHERE 
relname = 'performance_test'

EQUAL TO SIZE DIVIDED BY 8192

SELECT relpages, pg_relation_size('performance_test')/8192
FROM pg_class
WHERE relname = 'performance_test';

HOW TO FIND I/O COST USED BY PLAN

SHOW seq_page_cost;

TOTAL PREDICTED I/O COSTS

SELECT relpages * current_setting('seq_page_cost')::integer
FROM
pg_class
WHERE relname='performance_test'

CPU Costs Depends on Rows Processed

How to Find Rows in Table:
SELECT reltuples
FROM pg_class
WHERE relname='performance_test';

HOW TO FIND CPU COST USED BY PLAN

SHOW cpu_tuple_cost;

SHOW cpu_operator_cost;

TOTAL PREDICTED CPU COSTS
SELECT 
relpages * current_setting('seq_page_cost')::numeric + 
reltuples * current_setting('cpu_tuple_cost')::numeric + 
reltuples * current_setting('cpu_oerator_cost')::numeric
FROM
pg_class
WHERE relname = 'performance_test';

SOME ADDITIONAL COSTS CONSIDERATIONS

Cost of setting up each thread:
SHOW parallel_setup_cost;

Cost of communicating each row:
SHOW parallel_tuple_cost;

