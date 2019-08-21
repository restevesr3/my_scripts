--Add Not null constraint to order_details

ALTER TABLE order_details
ALTER COLUMN discount SET NOT NULL;
