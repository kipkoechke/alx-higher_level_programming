-- Create the database user 'user_0d_1' at the 'localhost' host and set the password.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables to 'user_0d_1' at the 'localhost' host.
GRANT ALL PRIVILEGES ON *.*
    TO 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';

-- Ensure that the privileges are refreshed to apply the changes immediately.
FLUSH PRIVILEGES;
