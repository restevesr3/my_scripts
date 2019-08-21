/*
3 Phases in Database Design

1. Requirement Analysis
2. Data Modeling
3. Normalization

Consequences of Bad Design
1. Don't have the information you need
2. Information is lost
3. Inaccurate information is recorded

Data vs. Information
- Data: Will Bunker 60 Lake Village
- Information: Instructor: Will Bunker, Heart Rate:60, Current location 
city: Lake Village
Process is to create a design that turns data into information

Requirements Analysis
- Answering the question: "What is the database going to be used for?"
- Talking to everyone using the system and finding out what information they
want
- What decisions need to be made?

Dating as Example
- People want to date someone:
	- in a certain age range
	- near them physically
	- from a certain culture
	The better we modeled this, the more money we made
	
Design Phase
- Define fields
- Assign to tables
- Design primary keys
- Establish relationships via foreign keys

Tools:
Entity Relationship Diagrams

Each Table Represents Either
1. An object: product, customer, supplier
2. An event: order, cancellation, meeting

3 Types of Relationships
1. One-to-One: like profile and description (split due to impact on searching)
2. One-to-Many: order to order_details
3. Many-to-Many: actors and movies

3 Types of fields in Bad Desgin
1. Multiplart field - like full name
2. Multivalued field - Children array
3. Calculated field - Total spent that is price * quantity

All this is called 
Normalization
- Eliminating duplicate/redundant data
- Breaking large tables into smaller ones
- Making sure that inserting/updating/deleting data doesn't cause problems

Normalization Can Seem Technical
Uses a lot of strange terminology, but boils down to reducing redundancy
and protecting from mistakes that would render data useless

Example: Deleting orders that had order details. Now wouldn't know who
placed the order.

Example: Having 5 fields for phone numbers in a customer table.
*/