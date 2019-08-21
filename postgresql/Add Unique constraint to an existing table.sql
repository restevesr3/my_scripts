-- Add Unique constraint to an existing table

ALTER TABLE region
ADD CONSTRAINT uq_region_description_region UNIQUE (regiondescription);