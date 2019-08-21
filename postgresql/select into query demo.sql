

CREATE TABLE IF NOT EXISTS performance_test
(
id serial,
location text
);

INSERT INTO performance_test(location)
SELECT 'Katmandu, Nepal'
FROM
generate_series(1, 10000000);
