-- create the MYSQL server user user_0d_1 with password user_0d_1_pwd
-- creates a new user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- grant all privileges to this user
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
