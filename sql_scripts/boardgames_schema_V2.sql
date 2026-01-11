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
    name VARCHAR(255) NOT NULL
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
    url VARCHAR(255),
    description VARCHAR(255),
    total_plays BIGINT,
    amazon_price FLOAT(53),
    wishlisted BIGINT,
    complexity FLOAT(53),
    num_ratings BIGINT,
    avg_rating FLOAT(53),
    player_id BIGINT,
    playtime_id BIGINT,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (playtime_id) REFERENCES playtime(playtime_id)
);

DROP TABLE IF EXISTS game_to_category;

CREATE TABLE game_to_category(
    id BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    game_id BIGINT NOT NULL,
    category_id BIGINT,
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)    
);

