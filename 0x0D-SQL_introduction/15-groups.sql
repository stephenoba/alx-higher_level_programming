-- lists the number of records that have same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score;
