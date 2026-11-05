use ironhack_idol;
SET GLOBAL local_infile = ON;
SELECT * FROM IMPORT_ALBUM_DATA;
SELECT count(*) FROM import_album_data;
SELECT count(*) FROM import_track_data;
SELECT * FROM import_track_data;
SHOW CREATE TABLE import_album_data;
SHOW VARIABLES LIKE 'local_infile';