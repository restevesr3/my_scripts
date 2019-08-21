--ALTER TABLE to ADD A NOT NULL CONSTRAINT

SELECT lastname
FROM
employees as e
WHERE 
lastname is NULL;

alter table employees
alter column lastname SET NOT NULL;