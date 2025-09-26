CREATE DATABASE IF NOT EXISTS boardgames;

USE boardgames;

DROP TABLE IF EXISTS players;

CREATE TABLE players(
    player_id BIGINT NOT NULL PRIMARY KEY,
    min_players BIGINT NOT NULL,
    max_players BIGINT NOT NULL,
    minimum_age BIGINT NOT NULL
);

DROP TABLE IF EXISTS categories;

CREATE TABLE categories(
    category_id BIGINT NOT NULL PRIMARY KEY,
    name BIGINT NOT NULL
);

DROP TABLE IF EXISTS playtime;

CREATE TABLE playtime(
    playtime_id BIGINT NOT NULL PRIMARY KEY,
    min_playtime BIGINT NOT NULL,
    max_playtime BIGINT NOT NULL
);

DROP TABLE IF EXISTS games;

CREATE TABLE games(
    game_id BIGINT NOT NULL PRIMARY KEY,
    boardgame VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    total_plays BIGINT NOT NULL,
    amazon_price FLOAT(53) NOT NULL,
    wishlisted BIGINT NOT NULL,
    complexity FLOAT(53) NOT NULL,
    num_ratings BIGINT NOT NULL,
    avg_rating FLOAT(53) NOT NULL,
    player_id BIGINT,
    playtime_id BIGINT,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (playtime_id) REFERENCES playtime(playtime_id)
);

DROP TABLE IF EXISTS game_to_category;

CREATE TABLE game_to_category(
    id BIGINT NOT NULL PRIMARY KEY,
    game_id BIGINT NOT NULL,
    category_id BIGINT,
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)    
);

