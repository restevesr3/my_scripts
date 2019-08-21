-- CREATE EXPRESSION INDEX ON CONCATENATED FIELD
create index idx_person_full_name
on person.person((firstname || ' ' || lastname));

EXPLAIN SELECT *
FROM
person.person
WHERE (firstname || ' ' || lastname) = 'Terri Duffy';

