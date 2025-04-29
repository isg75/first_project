DROP DATABASE IF EXISTS aivshuman;
CREATE DATABASE aivshuman;
USE aivshuman;

-- OCCUPATION GROWTH
DROP TABLE IF EXISTS occupation_growth;
CREATE TABLE occupation_growth (
  occupation_code VARCHAR(100) PRIMARY KEY,
  occupation_title VARCHAR(255),
  employment_2023 FLOAT,
  employment_2033 FLOAT,
  employment_change_2023_2033 FLOAT,
  employment_percent_change_2023_2033 FLOAT
);

-- AI JOB SENTIMENT
DROP TABLE IF EXISTS ai_job_sentiment;

CREATE TABLE `ai_job_sentiment` (
  `comment_id` VARCHAR(255),
  `comment_body` VARCHAR(255),
  `comment_score` INT,
  `comment_author` VARCHAR(255),
  `post_title` VARCHAR(255),
  `sentiment_label` VARCHAR(255),
  `occupation_code` VARCHAR(100),
  PRIMARY KEY (`comment_id`),
  FOREIGN KEY (`occupation_code`) REFERENCES `occupation_growth`(`occupation_code`)
);

-- OCCUPATION WAGES
DROP TABLE IF EXISTS occupation_wages;

CREATE TABLE `occupation_wages` (
  `id` INT AUTO_INCREMENT,
  `tot_emp` FLOAT,
  `a_mean` FLOAT,
  `h_mean` FLOAT,
  `sector` VARCHAR(255),
  `occupation_code` VARCHAR(100),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`occupation_code`) REFERENCES `occupation_growth`(`occupation_code`)

);


-- COUNTRY AI ADOPTION
DROP TABLE IF EXISTS country_ai_adoption;
CREATE TABLE country_ai_adoption (
  id INT PRIMARY KEY,
  country_id INT,
  sector VARCHAR(255),
  time_period INT,
  measure VARCHAR(255),
  observation_value FLOAT,
  FOREIGN KEY (country_id) REFERENCES country(country_id)
);

-- SECTOR TABLE
DROP TABLE IF EXISTS sector;
CREATE TABLE sector (
  sector_id INT PRIMARY KEY,
  sector_name VARCHAR(255),
  occupation_code VARCHAR(100),
  FOREIGN KEY (occupation_code) REFERENCES occupation_growth(occupation_code)
);
-- COUNTRY TABLE
DROP TABLE IF EXISTS country;
CREATE TABLE country (
  country_id INT PRIMARY KEY,
  country_name VARCHAR(255)
);

