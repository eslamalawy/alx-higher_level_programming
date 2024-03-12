-- displays the max temperature of each state (ordered by State name)
-- displays the max value of a column in a table
SELECT `state`, MAX(`value`) 'max_temp' FROM `temperatures` GROUP BY `state` ORDER BY `state` ASC;
