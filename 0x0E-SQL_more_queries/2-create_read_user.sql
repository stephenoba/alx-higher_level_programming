-- creates the database hbtn_0d_2 and the user user_0d_2.
--    set privilege for user_0d_2 to SELECT on database hbtn_0d_2
--    alter user_0d_2 password to user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER
	IF NOT EXISTS 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
