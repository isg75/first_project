Create database mental_issues;

CREATE TABLE `person`(
    `person_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `age` INT NOT NULL,
    `gender` VARCHAR(255) NOT NULL,
    `date` DATE NOT NULL,
    `industry_id` INT NOT NULL,
    `job_id` INT NOT NULL
);
CREATE TABLE `mental`(
    `mental_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Mental_Health_Status` VARCHAR(255) NOT NULL,
    `Burnout_Level` VARCHAR(255) NOT NULL,
    `Work_Life_Balance_Score` INT NOT NULL,
    `Physical_Health_Issues` VARCHAR(255) NOT NULL,
    `Social_Isolation_Score` INT NOT NULL
);
CREATE TABLE `job`(
    `job_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `job_role` VARCHAR(255) NOT NULL,
    `region` VARCHAR(255) NOT NULL,
    `salary_rate` VARCHAR(255) NOT NULL,
    `work_arrangement` VARCHAR(255) NOT NULL,
    `hours_per_week` INT NOT NULL,
    `industry_name` VARCHAR(255) NOT NULL
);
CREATE TABLE `mental_per_person`(
    `mental_per_person_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `mental_id` INT NOT NULL,
    `person_id` INT NOT NULL
);
ALTER TABLE
    `person` ADD CONSTRAINT `person_job_id_foreign` FOREIGN KEY(`job_id`) REFERENCES `job`(`job_id`);
ALTER TABLE
    `mental_per_person` ADD CONSTRAINT `mental_per_person_person_id_foreign` FOREIGN KEY(`person_id`) REFERENCES `person`(`person_id`);
ALTER TABLE
    `mental_per_person` ADD CONSTRAINT `mental_per_person_mental_id_foreign` FOREIGN KEY(`mental_id`) REFERENCES `mental`(`mental_id`);