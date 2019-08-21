--Expression Index demo 1
CREATE INDEX idx_product_upper_name
on production.product (UPPER(name));