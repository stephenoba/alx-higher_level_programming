-- lists all records of the table second_table of the database hbtn_0c_0
-- 	Results display both the score and the name
-- 	Records should be ordered by score (top first) 
SELECT score, name FROM second_table
WHERE `score`>=10
ORDER BY score DESC;
