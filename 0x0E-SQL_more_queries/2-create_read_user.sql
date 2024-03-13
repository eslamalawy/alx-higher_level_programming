-- create a database hbtn_0d_2 and the user user_0d_2
-- creates a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create a new user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grant priviledges to this user
GRANT SELECT ON hbtn_0d_2.*
TO user_0d_2@localhost;
