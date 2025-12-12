use hufflepuff;

CREATE TABLE IF NOT EXISTS population_data (
    postal_code INT,
    district VARCHAR(50),
    total INT,
    age_under_6 INT,
    age_6_to_15 INT,
    age_15_to_18 INT,
    age_18_to_27 INT,
    age_27_to_45 INT,
    age_45_to_55 INT,
    age_55_to_65 INT,
    age_65_plus INT,
    female_total INT
);


CREATE TABLE IF NOT EXISTS location_bridge (
    district VARCHAR(50),
    code INT,
    location VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS crime_data (
    year INT,
    district VARCHAR(50),
    code INT,
    location VARCHAR(255),
    robbery INT,
    street_robbery INT,
    injury INT,
    agg_assault INT,
    threat INT,
    theft INT,
    car INT,
    from_car INT,
    bike INT,
    burglary INT,
    fire INT,
    arson INT,
    damage INT,
    graffiti INT,
    drugs INT,
    local INT
);
