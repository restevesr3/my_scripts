SELECT 
pg_relation_size('performance_test'),
pg_size_pretty(pg_relation_size('performance_test'))

select 
relpages
FROM
pg_class
WHERE 
relname = 'performance_test'

SELECT relpages, pg_relation_size('performance_test')/8192
FROM pg_class
WHERE relname = 'performance_test';

SHOW seq_page_cost;

SELECT relpages * current_setting('seq_page_cost')::numeric,
reltuples
FROM
pg_class
WHERE relname='performance_test'

SHOW cpu_tuple_cost; --when the row in being put into the cpu (more expensive)

SHOW cpu_operator_cost; --when it is running in the cpu