-- Create the 'hbtn_0d_usa' database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create the 'states' table in the 'hbtn_0d_usa' database.
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
);
