--create index for pattern matching
CREATE INDEX trgm_idx_performance_test_location
ON performance_test USING gin (location gin_trgm_ops);

CREATE INDEX idx_performance_test_name
ON performance_test (name);