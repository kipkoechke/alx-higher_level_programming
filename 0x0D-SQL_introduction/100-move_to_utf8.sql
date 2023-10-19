-- Update the character set of the 'hbtn_0c_0' database to UTF-8.
USE `hbtn_0c_0`;

-- Modify the character set and collation for the 'first_table' in 'hbtn_0c_0'.
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
