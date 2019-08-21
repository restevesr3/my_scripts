/*
Speeding up Text Matching

- Pattern Matching Is Slow On Regular Indexes

CREATE EXTENSION pg_trgm;  <--must be turned on per database
CREATE INDEX tgrm_idx_performance_test_location
ON performance_test USING gin (location_gin_trgm_ops);

CREATE INDEX idx_performance_test_name
ON performance_test(name);





*/