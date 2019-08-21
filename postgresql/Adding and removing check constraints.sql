--Adding and removing check constraints

SELECT
reorderlevel,
count(*) as freq

FROM
products
group by
reorderlevel


UPDATE products
SET reorderlevel = 0
WHERE
(
reorderlevel IS NULL
OR
reorderlevel < 0
);

ALTER TABLE products
ADD CHECK (reorderlevel >= 0);