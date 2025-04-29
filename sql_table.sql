create database netflix;
use netflix;
-- Create database (optional)
CREATE DATABASE IF NOT EXISTS netflix_db;
USE netflix_db;

-- Create the table
drop table if exists Show_Directors;
drop table if exists Show_Cast;
drop table if exists Show_Countries;
drop table if exists Show_Genres;
drop table if exists Directors;
drop table if exists Cast;
drop table if exists Countries;
drop table if exists Genres;
drop table if exists shows;
drop table if exists platform;


CREATE TABLE shows (
    show_id VARCHAR(20) PRIMARY KEY,
    type VARCHAR(20) not null,
    title VARCHAR(255) NOT NULL,
    director TEXT,
    cast TEXT,
    country TEXT,
    date_added DATE,
    release_year INT,
    rating VARCHAR(10),
    duration VARCHAR(50),
    listed_in TEXT,
    description TEXT,
    duration_int INT,
    duration_type VARCHAR(20),
    genres TEXT,
    platform varchar(25)
);
describe shows;
select * from shows limit 10;

CREATE TABLE Directors (
    director_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE
);
select * from Directors;
CREATE TABLE Cast (
    cast_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE
);
select * from Cast;
CREATE TABLE Countries (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE
);
select * from Countries;
CREATE TABLE Genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE
);
select * from Genres;
CREATE TABLE Show_Directors (
    show_id VARCHAR(20),
    director_id INT,
    PRIMARY KEY (show_id, director_id),
    FOREIGN KEY (show_id) REFERENCES Shows(show_id),
    FOREIGN KEY (director_id) REFERENCES Directors(director_id)
);
select * from Show_Directors;
CREATE TABLE Show_Cast (
    show_id VARCHAR(20),
    cast_id INT,
    PRIMARY KEY (show_id, cast_id),
    FOREIGN KEY (show_id) REFERENCES Shows(show_id),
    FOREIGN KEY (cast_id) REFERENCES Casts(cast_id)
);
select * from Show_Cast;
CREATE TABLE Show_Countries (
    show_id VARCHAR(20),
    country_id INT,
    PRIMARY KEY (show_id, country_id),
    FOREIGN KEY (show_id) REFERENCES Shows(show_id),
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
);
select * from Show_Countries;
CREATE TABLE Show_Genres (
    show_id VARCHAR(20),
    genre_id INT,
    PRIMARY KEY (show_id, genre_id),
    FOREIGN KEY (show_id) REFERENCES Shows(show_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);
select * from Show_Genres;
