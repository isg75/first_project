CREATE TABLE IF NOT EXISTS `fact_energy` (
	`ener_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`prct_access_elec` FLOAT NOT NULL,
	`prim_ener_cons` FLOAT NOT NULL,
	`prct_renew_prod` FLOAT NOT NULL,
	`prct_renew_cons` FLOAT NOT NULL,
	PRIMARY KEY(`ener_id`)
);


CREATE TABLE IF NOT EXISTS `fact_emissions` (
	`emi_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`co2` FLOAT NOT NULL,
	`co2_luc` FLOAT NOT NULL,
	PRIMARY KEY(`emi_id`)
);


CREATE TABLE IF NOT EXISTS `fact_economy` (
	`eco_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`population` FLOAT NOT NULL,
	`gdp` FLOAT NOT NULL,
	`gdp_per_cap` FLOAT NOT NULL,
	PRIMARY KEY(`eco_id`)
);


CREATE TABLE IF NOT EXISTS `region` (
	`region_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`region_name` VARCHAR(255) NOT NULL,
	`iso_code` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`region_id`)
);


CREATE TABLE IF NOT EXISTS `country` (
	`country_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`country_name` VARCHAR(255) NOT NULL,
	`ener_id` BIGINT NOT NULL,
	`emi_id` BIGINT NOT NULL,
	`eco_id` BIGINT NOT NULL,
	`region_id` BIGINT NOT NULL,
	PRIMARY KEY(`country_id`)
);


ALTER TABLE `country`
ADD FOREIGN KEY(`emi_id`) REFERENCES `fact_emissions`(`emi_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `country`
ADD FOREIGN KEY(`eco_id`) REFERENCES `fact_economy`(`eco_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `fact_energy`
ADD FOREIGN KEY(`ener_id`) REFERENCES `country`(`ener_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `country`
ADD FOREIGN KEY(`region_id`) REFERENCES `region`(`region_id`)
ON UPDATE CASCADE ON DELETE CASCADE;