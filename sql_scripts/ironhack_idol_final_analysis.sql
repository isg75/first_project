USE ironhack_idol_main;
SELECT COUNT(*) FROM track_data;

-- Join tracks with albums
SELECT
    t.track_name,
    t.track_popularity,
    a.album_name,
    a.album_type,
    a.album_release_year
FROM track_data AS t
INNER JOIN album_data AS a
    ON t.album_id = a.album_id;
    
    -- Show the most popular tracks and their album_type
    SELECT
    t.track_name,
    t.track_popularity,
    a.album_name,
    a.album_type
FROM track_data AS t
INNER JOIN album_data AS a
    ON t.album_id = a.album_id
ORDER BY t.track_popularity DESC
LIMIT 10;

-- Join artist_ and tracks
SELECT
    ar.artist_name,
    t.track_name,
    t.track_popularity
FROM track_data AS t
JOIN artist_data AS ar
    ON t.artist_id = ar.artist_id;
    
    -- Join all three tables
    SELECT
    ar.artist_name,
    ar.main_genre,
    t.track_name,
    t.track_popularity,
    a.album_name,
    a.album_type,
    a.album_release_year
FROM track_data AS t
JOIN artist_data AS ar
    ON t.artist_id = ar.artist_id
JOIN album_data AS a
    ON t.album_id = a.album_id
LIMIT 20;


-- Find promising artists
SELECT
    ar.artist_name,
    ar.artist_followers,
    ar.artist_popularity,
    COUNT(DISTINCT t.track_id) AS number_of_tracks,
    ROUND(AVG(t.track_popularity), 2) AS average_track_popularity
FROM artist_data AS ar
JOIN track_data AS t
    ON ar.artist_id = t.artist_id
WHERE ar.artist_followers < 500000
GROUP BY
    ar.artist_id,
    ar.artist_name,
    ar.artist_followers,
    ar.artist_popularity
HAVING COUNT(DISTINCT t.track_id) >= 2
ORDER BY average_track_popularity DESC;

-- Left join
SELECT *
    -- t.track_name,
    -- a.album_name
FROM track_data AS t
LEFT JOIN album_data AS a
    ON t.album_id = a.album_id;

SELECT
    t.track_name,
    a.album_name
FROM track_data AS t
RIGHT JOIN album_data AS a
    ON t.album_id = a.album_id;
    
    SELECT *
    -- ar.artist_name,
   -- t.track_name,
   -- t.track_popularity
FROM track_data AS t
RIGHT JOIN artist_data AS ar
    ON t.artist_id = ar.artist_id;