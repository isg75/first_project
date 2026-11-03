CREATE DATABASE IF NOT EXISTS awards;
Use awards;
CREATE TABLE IF NOT EXISTS `albums` (
	`album_id` BIGINT NOT NULL AUTO_INCREMENT,
	`album_name` VARCHAR(255) NOT NULL,
	`release_year` BIGINT NOT NULL,
	PRIMARY KEY(`album_id`)
);


CREATE TABLE IF NOT EXISTS `tracks` (
	`track_id` VARCHAR(22) NOT NULL,
	`track_name` VARCHAR(255) NOT NULL,
	`track_popularity` BIGINT NOT NULL,
	`album_id` BIGINT NOT NULL,
	PRIMARY KEY(`track_id`)
);


CREATE TABLE IF NOT EXISTS `genres` (
	`genre_id` BIGINT NOT NULL AUTO_INCREMENT,
	`genre` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`genre_id`)
);


CREATE TABLE IF NOT EXISTS `artists` (
	`artist_name` VARCHAR(100) NOT NULL,
	`artist_popularity` TINYINT NOT NULL,
	`artist_followers` INTEGER NOT NULL,
	PRIMARY KEY(`artist_name`)
);


CREATE TABLE IF NOT EXISTS `track_artist` (
	`track_id` VARCHAR(22) NOT NULL,
	`artist_name` VARCHAR(100) NOT NULL,
	PRIMARY KEY(`track_id`, `artist_name`)
);


CREATE TABLE IF NOT EXISTS `artist_genre` (
	`genre_id` BIGINT NOT NULL,
	`artist_name` VARCHAR(100) NOT NULL,
	PRIMARY KEY(`genre_id`, `artist_name`)
);


ALTER TABLE `tracks`
ADD FOREIGN KEY(`album_id`) REFERENCES `albums`(`album_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `track_artist`
ADD FOREIGN KEY(`track_id`) REFERENCES `tracks`(`track_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `track_artist`
ADD FOREIGN KEY(`artist_name`) REFERENCES `artists`(`artist_name`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `artist_genre`
ADD FOREIGN KEY(`genre_id`) REFERENCES `genres`(`genre_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `artist_genre`
ADD FOREIGN KEY(`artist_name`) REFERENCES `artists`(`artist_name`)
ON UPDATE CASCADE ON DELETE CASCADE;