CREATE TABLE IF NOT EXISTS `track_data` (
	`track_id` VARCHAR(255) NOT NULL UNIQUE,
	`artist_id` BIGINT NOT NULL,
	`album_id` VARCHAR(255) NOT NULL,
	`track_name` VARCHAR(255) NOT NULL,
	`track_popularity` BIGINT NOT NULL,
	`track_duration_ms` BIGINT NOT NULL,
	PRIMARY KEY(`track_id`)
);


CREATE TABLE IF NOT EXISTS `artist_data` (
	`artist_id` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
	`artist_name` VARCHAR(255) NOT NULL UNIQUE,
	`artist_popularity` BIGINT NOT NULL,
	`artist_genres` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`artist_id`)
);


CREATE TABLE IF NOT EXISTS `album_data` (
	`album_id` VARCHAR(255) NOT NULL UNIQUE,
	`album_name` VARCHAR(255) NOT NULL,
	`album_type` VARCHAR(255) NOT NULL,
	`album_year` BIGINT NOT NULL,
	PRIMARY KEY(`album_id`)
);


ALTER TABLE `album_data`
ADD FOREIGN KEY(`album_id`) REFERENCES `track_data`(`album_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `artist_data`
ADD FOREIGN KEY(`artist_id`) REFERENCES `track_data`(`artist_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;