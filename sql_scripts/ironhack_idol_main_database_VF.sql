USE ironhack_idol_main;
LOAD DATA LOCAL INFILE
'C:/Users/JACOB/Documents/ironhack/Week_4/Day_1/first_project/data/clean/artist_data.csv'
INTO TABLE artist_data
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
SELECT * FROM artist_data;

LOAD DATA LOCAL INFILE
'C:/Users/JACOB/Documents/ironhack/Week_4/Day_1/first_project/data/clean/album_data.csv'
INTO TABLE album_data
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    album_id,
    album_name,
    album_type,
    album_release_year
);
SELECT * FROM album_data;
SELECT COUNT(*) FROM album_data;
SHOW VARIABLES LIKE 'local_infile';
DESCRIBE album_data;

LOAD DATA LOCAL INFILE
'C:/Users/JACOB/Documents/ironhack/Week_4/Day_1/first_project/data/clean/track_data.csv'
INTO TABLE track_data
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    track_id,
    artist_id,
    album_id,
    track_name,
    track_popularity,
    track_duration_min
);
SELECT * FROM track_data;
DESCRIBE track_data;
