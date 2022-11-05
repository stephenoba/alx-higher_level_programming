-- lists all the cities of California that can
-- be found in the database hbtn_0d_usa
SELECT 	id, name
FROM	cities c
WHERE	(SELECT id FROM states
	WHERE name = "California") = c.state_id
ORDER BY id;
