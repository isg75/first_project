DROP DATABASE IF EXISTS traficking_victims; 
CREATE DATABASE IF NOT EXISTS traficking_victims;
USE traficking_victims;

-- Region
CREATE TABLE `Region` (
  `Region_id` INT  ,
  `Region_name` VARCHAR(200),
  PRIMARY KEY (`Region_id`)
);

--  Subregion
CREATE TABLE `Subregion` (
  `Subregion_id` INT AUTO_INCREMENT,
  `Subregion_name` VARCHAR(200),
  `Region_id` INT ,
  PRIMARY KEY (`Subregion_id`),
  FOREIGN KEY (`Region_id`) REFERENCES `Region`(`Region_id`)
);

--  Country
CREATE TABLE `Country` (
  `Country_id` INT AUTO_INCREMENT,
  `Country_name` VARCHAR(200),
  `Subregion_id` INT,
  PRIMARY KEY (`Country_id`),
  FOREIGN KEY (`Subregion_id`) REFERENCES `Subregion`(`Subregion_id`)
);

--  Victim
CREATE TABLE `Victim` (
  `Victim_id` INT AUTO_INCREMENT,
  `Sex` VARCHAR(200),
  `Age` VARCHAR(200),
  PRIMARY KEY (`Victim_id`)
);

--  Offense
CREATE TABLE `Offense` (
  `Offense_id` INT AUTO_INCREMENT,
  `Year` YEAR,
  `Dimension` VARCHAR(200),
  `Category` VARCHAR(200),
  `Nr_of_victims` VARCHAR(200),
  `Country_id` INT,
  `Victim_id` INT,
  PRIMARY KEY (`Offense_id`),
  FOREIGN KEY (`Country_id`) REFERENCES `Country`(`Country_id`),
  FOREIGN KEY (`Victim_id`) REFERENCES `Victim`(`Victim_id`)
);