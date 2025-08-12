CREATE TABLE `job`(
    `job_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `job_title` VARCHAR(255) NOT NULL,
    `salary_usd` INT NOT NULL,
    `education_required` VARCHAR(255) NOT NULL,
    `employee_type` VARCHAR(255) NOT NULL,
    `employee_id` INT NOT NULL,
    `company_id` INT NOT NULL,
    `remote_ratio` INT NOT NULL,
    `required_skills` VARCHAR(255) NOT NULL,
    `salary_currency` VARCHAR(255) NOT NULL,
    `posting_date` DATE NOT NULL,
    `benefits_score` FLOAT(53) NOT NULL
);
CREATE TABLE `employee`(
    `employee_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `employee_residence` VARCHAR(255) NOT NULL,
    `experience_level` VARCHAR(255) NOT NULL,
    `years_experience` INT NOT NULL
);
CREATE TABLE `company`(
    `company_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `company_location` VARCHAR(255) NOT NULL,
    `company_name` VARCHAR(255) NOT NULL,
    `company_size` VARCHAR(255) NOT NULL,
    `industry` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `job` ADD CONSTRAINT `job_company_id_foreign` FOREIGN KEY(`company_id`) REFERENCES `company`(`company_id`);
ALTER TABLE
    `job` ADD CONSTRAINT `job_employee_id_foreign` FOREIGN KEY(`employee_id`) REFERENCES `employee`(`employee_id`);