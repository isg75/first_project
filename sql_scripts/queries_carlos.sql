use hufflepuff;


# 
#-------------------------------------------------------------------------------------

#Total crimes per district

SELECT district, SUM(robbery + street_robbery + injury + agg_assault + threat + theft +
                     car + from_car + bike + burglary + fire + arson + damage + graffiti +
                     drugs + local) AS total_crime
FROM crime_data
GROUP BY district
ORDER BY total_crime DESC;

#Total crimes per district per year

SELECT year, district,
       SUM(robbery + street_robbery + injury + agg_assault + threat + theft +
           car + from_car + bike + burglary + fire + arson + damage +
           graffiti + drugs + local) AS total_crime
FROM crime_data
GROUP BY year, district
ORDER BY year, total_crime DESC;

# Most dangerous locations

SELECT location,
       SUM(robbery + street_robbery + injury + agg_assault + threat + theft +
           car + from_car + bike + burglary + fire + arson + damage +
           graffiti + drugs + local) AS total_crime
FROM crime_data
GROUP BY location
ORDER BY total_crime DESC
LIMIT 20;


# Crimes per 1,000 residents

SELECT c.code,
       c.location,
       SUM(robbery + street_robbery + injury + agg_assault + threat + theft +
           car + from_car + bike + burglary + fire + arson + damage +
           graffiti + drugs + local) AS crimes,
       p.total AS population,
       ROUND(
         SUM(robbery + street_robbery + injury + agg_assault + threat +
             theft + car + from_car + bike + burglary + fire + arson +
             damage + graffiti + drugs + local) / p.total * 1000, 2
       ) AS crimes_per_1000
FROM crime_data c
JOIN population_data p ON c.code = p.postal_code
GROUP BY c.code, c.location, p.total
ORDER BY crimes_per_1000 DESC;


# violent crimes per district

SELECT 
    district,
    SUM(robbery + street_robbery + injury + agg_assault + threat) AS violent_crime
FROM crime_data
GROUP BY district
ORDER BY violent_crime DESC;

# theft related crimes 

SELECT 
    district,
    SUM(theft + car + from_car + bike) AS theft_related_crimes
FROM crime_data
GROUP BY district
ORDER BY theft_related_crimes DESC;


SELECT c.code, p.postal_code
FROM crime_data c
LEFT JOIN population_data p ON c.code = p.postal_code
WHERE p.postal_code IS NULL
LIMIT 20;

SELECT c.code, c.location
FROM crime_data c
LEFT JOIN population_data p
    ON CAST(c.code AS UNSIGNED) = CAST(p.postal_code AS UNSIGNED)
WHERE p.postal_code IS NULL;


# District crimes per 1000 residents

SELECT 
    LOWER(c.district) AS district,
    SUM(
        c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat +
        c.theft + c.car + c.from_car + c.bike + c.burglary + c.fire + 
        c.arson + c.damage + c.graffiti + c.drugs + c.local
    ) AS total_crimes,
    p.total AS population,
    ROUND(
        SUM(
            c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat +
            c.theft + c.car + c.from_car + c.bike + c.burglary + c.fire + 
            c.arson + c.damage + c.graffiti + c.drugs + c.local
        ) / p.total * 1000, 2
    ) AS crimes_per_1000
FROM crime_data c
JOIN population_data p
    ON LOWER(c.district) = LOWER(p.district)
GROUP BY district, p.total
ORDER BY crimes_per_1000 DESC;


# districts by crime type

SELECT 
    LOWER(c.district) AS district,
    SUM(c.robbery) AS robbery,
    SUM(c.theft) AS theft,
    SUM(c.agg_assault) AS agg_assault,
    SUM(c.street_robbery) AS street_robbery,
    p.total AS population,
    ROUND(SUM(c.robbery + c.street_robbery + c.agg_assault + c.theft) / p.total * 1000, 2) AS crimes_per_1000
FROM crime_data c
JOIN population_data p
    ON LOWER(c.district) = LOWER(p.district)
GROUP BY district, p.total
ORDER BY crimes_per_1000 DESC;

CREATE TEMPORARY TABLE population_unique AS
SELECT 
    LOWER(district) AS district,
    MAX(total) AS total
FROM population_data
GROUP BY LOWER(district);

SELECT 
    LOWER(c.district) AS district,
    SUM(c.robbery) AS robbery,
    SUM(c.street_robbery) AS street_robbery,
    SUM(c.injury) AS injury,
    SUM(c.agg_assault) AS agg_assault,
    SUM(c.threat) AS threat,
    SUM(c.theft) AS theft,
    SUM(c.car) AS car,
    SUM(c.from_car) AS from_car,
    SUM(c.bike) AS bike,
    SUM(c.burglary) AS burglary,
    SUM(c.fire) AS fire,
    SUM(c.arson) AS arson,
    SUM(c.damage) AS damage,
    SUM(c.graffiti) AS graffiti,
    SUM(c.drugs) AS drugs,
    SUM(c.local) AS local,
    p.total AS population
FROM crime_data c
JOIN population_unique p
    ON LOWER(c.district) = p.district
GROUP BY district, p.total
ORDER BY district;


# Age and Crime Correlation 

SELECT 
    p.district,
    SUM(p.age_18_to_27 + p.age_27_to_45) AS young_population,
    SUM(p.age_55_to_65 + p.age_65_plus) AS older_population,
    SUM(c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat) AS violent_crime
FROM population_data p
LEFT JOIN crime_data c
    ON LOWER(p.district) = LOWER(c.district)
GROUP BY p.district;

# violent crimes against young and older population

SELECT 
    p.district,
    SUM(p.age_18_to_27 + p.age_27_to_45) AS young_population,
    SUM(p.age_55_to_65 + p.age_65_plus) AS older_population,
    SUM(c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat) AS violent_crime
FROM population_data p
LEFT JOIN crime_data c
    ON LOWER(p.district) = LOWER(c.district)
GROUP BY p.district
ORDER BY violent_crime DESC;

# Specific crime type per age group

SELECT 
    p.district,
    SUM(p.age_18_to_27 + p.age_27_to_45) AS young_population,
    SUM(p.age_55_to_65 + p.age_65_plus) AS older_population,
    SUM(c.theft) AS general_theft,
    SUM(c.car) AS car_theft,
    SUM(c.from_car) AS theft_from_car,
    SUM(c.bike) AS bike_theft,
    SUM(c.theft + c.car + c.from_car + c.bike) AS total_theft
FROM population_data p
LEFT JOIN crime_data c
    ON LOWER(p.district) = LOWER(c.district)
GROUP BY p.district
ORDER BY total_theft DESC;

#  violent crime type per 1000 residents by age group

SELECT 
    p.district,
    SUM(p.age_18_to_27 + p.age_27_to_45) AS young_population,
    SUM(p.age_55_to_65 + p.age_65_plus) AS older_population,
    SUM(c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat) AS violent_crime,
    ROUND(SUM(c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat)
          / SUM(p.age_18_to_27 + p.age_27_to_45) * 1000, 2) AS violent_per_1000_young,
    ROUND(SUM(c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat)
          / SUM(p.age_55_to_65 + p.age_65_plus) * 1000, 2) AS violent_per_1000_older
FROM population_data p
LEFT JOIN crime_data c
    ON LOWER(p.district) = LOWER(c.district)
GROUP BY p.district;


#--------------------------------------------------------------------------------------------------

# H1 – General Crime Rate vs Population

-- Create a unique population per district
CREATE TEMPORARY TABLE population_unique AS
SELECT 
    LOWER(district) AS district,
    MAX(total) AS total
FROM population_data
GROUP BY LOWER(district);

-- Total crimes per district, aggregated
SELECT 
    LOWER(c.district) AS district,
    SUM(c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat +
        c.theft + c.car + c.from_car + c.bike + c.burglary + c.fire + 
        c.arson + c.damage + c.graffiti + c.drugs + c.local) AS total_crimes,
    p.total AS population,
    ROUND(SUM(c.robbery + c.street_robbery + c.injury + c.agg_assault + c.threat +
        c.theft + c.car + c.from_car + c.bike + c.burglary + c.fire + 
        c.arson + c.damage + c.graffiti + c.drugs + c.local) / p.total * 1000, 2) 
        AS crimes_per_1000
FROM crime_data c
JOIN population_unique p
    ON LOWER(c.district) = p.district
GROUP BY LOWER(c.district), p.total
ORDER BY total_crimes DESC;


# H2 – Regierungsviertel Threat & Damage

SELECT
    LOWER(c.district) AS district,
    ROUND(SUM(c.threat + c.damage) / SUM(p.total) * 1000, 2) AS threat_damage_per_1000
FROM crime_data c
JOIN population_data p
    ON LOWER(c.district) = LOWER(p.district)
GROUP BY LOWER(c.district)
ORDER BY threat_damage_per_1000 DESC;


# H3 – Older Population & Burglary

SELECT
    LOWER(p.district) AS district,
    SUM(p.age_55_to_65 + p.age_65_plus) AS older_population,
    SUM(c.burglary) AS total_burglary,
    ROUND(SUM(c.burglary) / SUM(p.age_55_to_65 + p.age_65_plus) * 1000, 2) AS burglary_per_1000_older
FROM population_data p
LEFT JOIN crime_data c
    ON LOWER(p.district) = LOWER(c.district)
GROUP BY district;

# H4 – Young Population & Drug Offenses

SELECT
    LOWER(p.district) AS district,
    SUM(p.age_18_to_27 + p.age_27_to_45) AS young_population,
    SUM(c.drugs) AS total_drugs,
    ROUND(SUM(c.drugs) / SUM(p.age_18_to_27 + p.age_27_to_45) * 1000, 2) AS drugs_per_1000_young
FROM population_data p
LEFT JOIN crime_data c
    ON LOWER(p.district) = LOWER(c.district)
GROUP BY district;

# H5 – Car Theft Trend Over Years

SELECT year, SUM(car) AS total_car_theft
FROM crime_data
GROUP BY year
ORDER BY year ASC;
