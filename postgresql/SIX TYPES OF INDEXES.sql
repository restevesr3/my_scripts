/*
SIX TYPES OF INDEXES
1. B-Tree: default index. When you create and index without specifying, this is
what you get. Works with comparison operators such as <,>,=, >=
2. Hash: Only handles equal operator, best used in id fields, takes less space
3. GIN: acronym for Generalized Inverted Index, useful for data types that have
multiple values in a column:
	- Arrays
	- Range types
	- JSONB
	- Hstore-key/value pairs
	They are aware of the internal data structure, so support for each type 
	must be added and it varies
	For arrays they can handle containment and overlap in addition to equality
	and comparison
	- @> and <@
	- &&
	
4. Gist: Generalized Inverted Search Tree. Useful when you have data that 
overlap with the value of that column - lige geometry or full text search

They have constraints around size but can be lossy and can produce false
matches with require PostgreSQL to do a check.

5. BRIN: Block Range Indexes. Best used for large datasets that have some
natural ordering - like time series or zip codes. The more sequential the
ordering the better.

6. SP-Gist: Space Partitioned GiST: useful for data that has a natural clustering
to it but not balanced. U.S. phone numbers are an example of this. Clustered
around area code, next 3 numbers for switch and the last four digits.

How to create an index:
CREATE INDEX <index_name>
ON <table_name> USING <index_type> (field1,...)
*/