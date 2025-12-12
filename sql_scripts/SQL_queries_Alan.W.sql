create database if not exists Hufflepuff;
use hufflepuff;
select * from berlin_crimes;
show tables;
SELECT 
    District,
    SUM(Robbery + Street_robbery + Injury + Agg_assault +
        Threat + Theft + Car + From_car + Bike +
        Burglary + Fire + Arson + Damage + Graffiti +
        Drugs + Local) AS total_crime
FROM berlin_crimes
GROUP BY District
ORDER BY total_crime DESC
LIMIT 5;
SELECT 
    District,
    SUM(Robbery + Street_robbery + Agg_assault + Injury + Threat)
      AS violent_crime
FROM berlin_crimes
GROUP BY District
ORDER BY violent_crime DESC
LIMIT 5;
describe population_berlin_clean;
SELECT 
    p.District,
    p.Year,
    SUM(c.Robbery + c.Street_robbery + c.Injury + c.Agg_assault +
        c.Threat + c.Theft + c.Car + c.From_car + c.Bike +
        c.Burglary + c.Fire + c.Arson + c.Damage + c.Graffiti +
        c.Drugs + c.Local) AS total_crime,
    p.Population,
    ROUND(
        SUM(c.Robbery + c.Street_robbery + c.Injury + c.Agg_assault +
            c.Threat + c.Theft + c.Car + c.From_car + c.Bike +
            c.Burglary + c.Fire + c.Arson + c.Damage + c.Graffiti +
            c.Drugs + c.Local) * 100000.0 / p.Population,
        1
    ) AS crime_per_100k
FROM berlin_crimes c
JOIN population_berlin_clean p
    ON p.District = c.District
   AND p.Year = c.Year
GROUP BY p.District, p.Year, p.Population
ORDER BY crime_per_100k DESC
LIMIT 5;
SELECT 
    p.district,
    SUM(c.Robbery + c.Street_robbery + c.Injury + c.Agg_assault +
        c.Threat + c.Theft + c.Car + c.From_car + c.Bike +
        c.Burglary + c.Fire + c.Arson + c.Damage + c.Graffiti +
        c.Drugs + c.Local) AS total_crime,
    p.total AS population,
    ROUND(
        SUM(c.Robbery + c.Street_robbery + c.Injury + c.Agg_assault +
            c.Threat + c.Theft + c.Car + c.From_car + c.Bike +
            c.Burglary + c.Fire + c.Arson + c.Damage + c.Graffiti +
            c.Drugs + c.Local) * 100000.0 / p.total,
        1
    ) AS crime_per_100k
FROM berlin_crimes c
JOIN population_berlin_clean p
    ON LOWER(c.District) = LOWER(p.district)
GROUP BY p.district, p.total
ORDER BY crime_per_100k DESC
LIMIT 5;
SELECT 
    District,
    SUM(Theft + Bike + From_car + Robbery + Street_robbery) AS tourist_risk_crime
FROM berlin_crimes
GROUP BY District
ORDER BY tourist_risk_crime DESC
LIMIT 5;
SELECT 
    District,
    SUM(Bike + Robbery + Street_robbery) AS nightlife_crime
FROM berlin_crimes
GROUP BY District
ORDER BY nightlife_crime DESC
LIMIT 10;
