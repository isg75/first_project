CREATE TABLE IF NOT EXISTS `property` (
	`property_id` BIGINT NOT NULL,
	`property_name` VARCHAR2(225) NOT NULL,
	`property_type_id` BIGINT NOT NULL,
	`country_id` BIGINT NOT NULL,
	`price` DECIMAL NOT NULL,
	`rating` FLOAT NOT NULL,
	`review_count` BIGINT NOT NULL,
	`location_id` BIGINT NOT NULL,
	PRIMARY KEY(`property_id`),
	CONSTRAINT `property_unique_0` UNIQUE (`property_id`)
);


CREATE TABLE IF NOT EXISTS `property_type` (
	`property_type__id` BIGINT NOT NULL,
	`property_type` VARCHAR2(225) NOT NULL,
	PRIMARY KEY(`property_type__id`),
	CONSTRAINT `property_type_unique_0` UNIQUE (`property_type__id`)
);


CREATE TABLE IF NOT EXISTS `country` (
	`country_id` BIGINT NOT NULL AUTO_INCREMENT,
	`country_name` VARCHAR2(225) NOT NULL,
	PRIMARY KEY(`country_id`),
	CONSTRAINT `country_unique_0` UNIQUE (`country_id`)
);


CREATE TABLE IF NOT EXISTS `amenities` (
	`amenity_id` BIGINT NOT NULL AUTO_INCREMENT,
	`amenity_name` VARCHAR2(225) NOT NULL,
	PRIMARY KEY(`amenity_id`),
	CONSTRAINT `amenities_unique_0` UNIQUE (`amenities_id`)
);


CREATE TABLE IF NOT EXISTS `property_amenity` (
	`property_id` BIGINT NOT NULL AUTO_INCREMENT,
	`amenity_id` BIGINT NOT NULL,
	PRIMARY KEY(`property_id`),
	CONSTRAINT `property_amenity_unique_0` UNIQUE (`property_id`)
);


CREATE TABLE IF NOT EXISTS `location` (
	`location_id` BIGINT NOT NULL AUTO_INCREMENT,
	`country_id` BIGINT NOT NULL,
	PRIMARY KEY(`location_id`),
	CONSTRAINT `location_unique_0` UNIQUE (`location_id`)
);


ALTER TABLE `property`
ADD FOREIGN KEY(`property_id`) REFERENCES `property_amenity`(`property_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `property_amenity`
ADD FOREIGN KEY(`amenity_id`) REFERENCES `amenities`(`amenity_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `property_type`
ADD FOREIGN KEY(`property_type__id`) REFERENCES `property`(`property_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `country`
ADD FOREIGN KEY(`country_id`) REFERENCES `property`(`country_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `location`
ADD FOREIGN KEY(`location_id`) REFERENCES `property`(`location_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `location`
ADD FOREIGN KEY(`country_id`) REFERENCES `property`(`country_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;