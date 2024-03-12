-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
-- groups rows together when they have the same scores and displays the number of occurrences
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
