use awards;

-- Update Albums Table
LOAD DATA LOCAL INFILE 'sql_scripts/albums_sql.csv'
INTO TABLE albums
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Update Tracks Table
LOAD DATA LOCAL INFILE 'sql_scripts/tracks_sql.csv'
INTO TABLE tracks
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Update Genres Table
LOAD DATA LOCAL INFILE 'sql_scripts/genres_sql.csv'
INTO TABLE genres
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Update Artists Table
LOAD DATA LOCAL INFILE 'sql_scripts/artist_sql.csv'
INTO TABLE artists
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Update Track-Artist Table
LOAD DATA LOCAL INFILE 'sql_scripts/track_artist_sql.csv'
INTO TABLE track_artist
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Update Artist_Genre Table
LOAD DATA LOCAL INFILE 'sql_scripts/artist_genre_sql.csv'
INTO TABLE artist_genre
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;