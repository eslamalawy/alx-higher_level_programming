-- script that updates the score of Bob to 10 in the table second_table.
UPDATE second_table
SET
score = 10
WHERE second_table.name = "Bob";
