INSERT INTO performance_test(location)
SELECT md5(random()::text) FROM generate_series(1, 10000000);