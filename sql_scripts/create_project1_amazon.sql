CREATE DATABASE IF NOT EXISTS project1_amazon;

USE project1_amazon;

DROP TABLE IF EXISTS `products`;

CREATE TABLE IF NOT EXISTS `products` (
	`product_id` VARCHAR(20) NOT NULL,
	`product_name` TEXT NOT NULL,
	`about_product` TEXT,
	`discounted_price` DECIMAL(10,2),
	`actual_price` DECIMAL(10,2),
	`discount_percentage` INTEGER,
	`rating` DECIMAL(3,2),
	`rating_count` INTEGER,
	`product_link` TEXT,
	PRIMARY KEY(`product_id`)
);

DROP TABLE IF EXISTS `categories`;

CREATE TABLE IF NOT EXISTS `categories` (
	`category_id` INTEGER NOT NULL AUTO_INCREMENT,
	`category_name` VARCHAR(255) NOT NULL,
	`sub_cat1` VARCHAR(255),
	`sub_cat2` VARCHAR(255),
	`sub_cat3` VARCHAR(255),
	PRIMARY KEY(`category_id`)
);

DROP TABLE IF EXISTS `product_categories`;

CREATE TABLE IF NOT EXISTS `product_categories` (
	`product_id` VARCHAR(20) NOT NULL,
	`category_id` INTEGER NOT NULL,
	PRIMARY KEY(`product_id`, `category_id`)
);

DROP TABLE IF EXISTS `users`;

CREATE TABLE IF NOT EXISTS `users` (
	`user_id` VARCHAR(100) NOT NULL,
	`user_name` VARCHAR(255),
	PRIMARY KEY(`user_id`)
);

DROP TABLE IF EXISTS `reviews`;

CREATE TABLE IF NOT EXISTS `reviews` (
	`review_id` VARCHAR(100) NOT NULL,
	`product_id` VARCHAR(20) NOT NULL,
	`user_id` VARCHAR(100) NOT NULL,
	`review_title` TEXT,
	`review_content` TEXT,
	PRIMARY KEY(`review_id`)
);

DROP TABLE IF EXISTS `product_images`;

CREATE TABLE IF NOT EXISTS `product_images` (
	`image_id` INTEGER NOT NULL AUTO_INCREMENT,
	`product_id` VARCHAR(20) NOT NULL,
	`image_url` TEXT,
	PRIMARY KEY(`image_id`)
);


ALTER TABLE `product_categories`
ADD FOREIGN KEY(`product_id`) REFERENCES `products`(`product_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `product_categories`
ADD FOREIGN KEY(`category_id`) REFERENCES `categories`(`category_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `reviews`
ADD FOREIGN KEY(`product_id`) REFERENCES `products`(`product_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `reviews`
ADD FOREIGN KEY(`user_id`) REFERENCES `users`(`user_id`)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `product_images`
ADD FOREIGN KEY(`product_id`) REFERENCES `products`(`product_id`)
ON UPDATE CASCADE ON DELETE CASCADE;