-- lists all records of the table second_table
-- 	Excludes row qithout a name
-- 	Display score and name in descending score order
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
