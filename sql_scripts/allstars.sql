CREATE TABLE IF NOT EXISTS `Restaurant` (
	`restaurant_id` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
	`restaurant_name` VARCHAR(255) NOT NULL,
	`city` VARCHAR(255) NOT NULL,
	`region` VARCHAR(255) NOT NULL,
	`url` VARCHAR(255) NOT NULL,
	`cuisine_id` BIGINT NOT NULL,
	PRIMARY KEY(`restaurant_id`)
);


CREATE TABLE IF NOT EXISTS `Stars rating` (
	`star_id` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
	`price_mean` FLOAT NOT NULL,
	`year` YEAR NOT NULL,
	`stars` INTEGER NOT NULL,
	`price_tag` VARCHAR(255) NOT NULL,
	`restaurant_id` BIGINT NOT NULL,
	PRIMARY KEY(`star_id`)
);


CREATE TABLE IF NOT EXISTS `Cuisine` (
	`cuisine_id` BIGINT NOT NULL,
	`price_mean` FLOAT NOT NULL,
	`cuisine_type` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`cuisine_id`)
);


ALTER TABLE `Stars rating`
ADD FOREIGN KEY(`restaurant_id`) REFERENCES `Restaurant`(`restaurant_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `Restaurant`
ADD FOREIGN KEY(`cuisine_id`) REFERENCES `Cuisine`(`cuisine_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

SELECT * FROM stars_df