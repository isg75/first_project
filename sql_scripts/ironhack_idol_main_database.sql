CREATE DATABASE ironhack_idol_main;
USE Ironhack_idol_main;
CREATE TABLE IF NOT EXISTS `track_data` (
	`track_id` VARCHAR(255) NOT NULL,
	`artist_id` BIGINT NOT NULL,
	`album_id` VARCHAR(255) NOT NULL,
	`track_name` VARCHAR(255) NOT NULL,
	`track_popularity` BIGINT NOT NULL,
	`track_duration_min` FLOAT NOT NULL,
	PRIMARY KEY(`track_id`)
);


CREATE TABLE IF NOT EXISTS `artist_data` (
	`artist_id` BIGINT NOT NULL UNIQUE,
	`artist_name` VARCHAR(255) NOT NULL UNIQUE,
	`artist_popularity` FLOAT NOT NULL,
	`artist_followers` FLOAT NOT NULL,
	`main_genre` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`artist_id`)
);


CREATE TABLE IF NOT EXISTS `album_data` (
	`album_id` VARCHAR(255) NOT NULL,
	`album_name` VARCHAR(255) NOT NULL,
	`album_type` VARCHAR(255) NOT NULL,
	`album_release_year` BIGINT NOT NULL,
	PRIMARY KEY(`album_id`)
);


ALTER TABLE `track_data`
ADD FOREIGN KEY(`album_id`) REFERENCES `album_data`(`album_id`)
ON UPDATE CASCADE ON DELETE NO ACTION;
ALTER TABLE `track_data`
ADD FOREIGN KEY(`artist_id`) REFERENCES `artist_data`(`artist_id`)
ON UPDATE CASCADE ON DELETE NO ACTION;