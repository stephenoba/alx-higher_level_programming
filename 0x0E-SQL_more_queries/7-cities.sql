-- creates the database hbtn_0d_usa and the table cities
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY state_id
		REFERENCES state(id),
	);
