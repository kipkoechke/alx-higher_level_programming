-- Create the database 'hbtn_0d_2' and the user 'user_0d_2'.
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_2`;

-- Create the user 'user_0d_2' at 'localhost' with the password 'user_0d_2_pwd'.
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database 'hbtn_0d_2' to 'user_0d_2' at 'localhost'.
GRANT SELECT
    ON `hbtn_0d_2`.*
    TO 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

-- Ensure that privileges are refreshed to apply the changes.
FLUSH PRIVILEGES;
