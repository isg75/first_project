USE berlincrimes;

ALTER TABLE `bridge`
ADD FOREIGN KEY(`code`) REFERENCES `population`(`postal_code`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `crime`
ADD FOREIGN KEY(`district_ID`) REFERENCES `bridge`(`district_ID`)
ON UPDATE NO ACTION ON DELETE NO ACTION;


SELECT District from crimes;

SELECT DISTINCT district
FROM population;




SELECT
    postal_code,
    COUNT(*) AS count_of_duplicates
FROM
    population
GROUP BY
    postal_code
HAVING
    COUNT(*) > 1;
    
SELECT
    District,
    COUNT(*) AS count_of_duplicates
FROM
    crimes
GROUP BY
    District
HAVING
    COUNT(*) > 1;
    
SELECT
    Location,
    COUNT(*) AS count_of_duplicates
FROM
    crimes
GROUP BY
    Location
HAVING
    COUNT(*) > 1;
    
SELECT
    Code,
    COUNT(*) AS count_of_duplicates
FROM
    crimes
GROUP BY
    Code
HAVING
    COUNT(*) > 1;
    
SELECT
    location,
    COUNT(*) AS count_of_duplicates
FROM
    locations
GROUP BY
    location
HAVING
    COUNT(*) > 1;



-- CRI Analysis by District

SELECT
    T1.district,
    ROUND(CAST(SUM(T2.Total_Crimes) AS REAL) / 7) AS Avg_Annual_Crimes,
    SUM(T1.total) AS Total_Population,
    ROUND((CAST(SUM(T2.Total_Crimes) AS REAL) / 7 * 1000) / SUM(T1.total)) AS Avg_Annual_Crime_Rate_per_1000
FROM
    Population T1
INNER JOIN
    (
        SELECT
            District,
            Code,
            Robbery + Street_robbery + Injury + Agg_assault + Threat + Theft + Car + From_car + Bike + Burglary + Fire + Arson + Damage + Graffiti + Drugs + Local AS Total_Crimes
        FROM
            Crimes
    ) T2 ON T1.district = T2.District
GROUP BY
    T1.district
ORDER BY
    Avg_Annual_Crime_Rate_per_1000 DESC;




-- Most and least common crime types

SELECT 'Robbery' AS Crime_Type, SUM(Robbery) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Street_robbery' AS Crime_Type, SUM(Street_robbery) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Injury' AS Crime_Type, SUM(Injury) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Agg_assault' AS Crime_Type, SUM(Agg_assault) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Threat' AS Crime_Type, SUM(Threat) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Theft' AS Crime_Type, SUM(Theft) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Car' AS Crime_Type, SUM(Car) AS Total_Count FROM Crimes
UNION ALL
SELECT 'From_car' AS Crime_Type, SUM(From_car) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Bike' AS Crime_Type, SUM(Bike) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Burglary' AS Crime_Type, SUM(Burglary) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Fire' AS Crime_Type, SUM(Fire) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Arson' AS Crime_Type, SUM(Arson) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Damage' AS Crime_Type, SUM(Damage) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Graffiti' AS Crime_Type, SUM(Graffiti) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Drugs' AS Crime_Type, SUM(Drugs) AS Total_Count FROM Crimes
UNION ALL
SELECT 'Local' AS Crime_Type, SUM(Local) AS Total_Count FROM Crimes
ORDER BY Total_Count DESC;




-- Demographic data
SELECT
    district,
    SUM(age_18_to_27) AS Total_Young_Adults,
    SUM(total) AS Total_Population,
    -- Calculate the percentage of the population in the 18-to-27 age group
    CAST(SUM(age_18_to_27) AS REAL) * 100 / SUM(total) AS Percent_Young_Adults
FROM
    Population
GROUP BY
    district
ORDER BY
    Percent_Young_Adults DESC;




-- crime tuypes per year
SELECT
    Year,
    SUM(Robbery) AS Total_Robbery,
    SUM(Street_robbery) AS Total_Street_Robbery,
    SUM(Agg_assault) AS Total_Agg_Assault,
    SUM(Threat) AS Total_Threat,
    SUM(Theft) AS Total_Theft,
    SUM(Car) AS Total_Car_Theft,
    SUM(From_car) AS Total_Theft_From_Car,
    SUM(Bike) AS Total_Bike_Theft,
    SUM(Burglary) AS Total_Burglary,
    SUM(Fire) AS Total_Fire,
    SUM(Arson) AS Total_Arson,
    SUM(Damage) AS Total_Damage,
    SUM(Graffiti) AS Total_Graffiti,
    SUM(Drugs) AS Total_Drugs
FROM
    crimes
GROUP BY
    Year
ORDER BY
    Year ASC;


-- CRIMES PER YEAR PER DISTRICT

SELECT
    Year,
    REPLACE(
        REPLACE(
            REPLACE(
                REPLACE(District, 'Ã¤', 'ae'), 
                'Ã¶', 'oe'
            ), 
            'Ã¼', 'ue'
        ),
        'ÃŸ', 'ss'
    ) AS Corrected_District,
    SUM(Robbery + Street_robbery + Injury + Agg_assault + Threat + Theft + Car + From_car + Bike + Burglary + Fire + Arson + Damage + Graffiti + Drugs + Local) AS Total_Crimes_Per_District_Year
FROM
    Crimes
GROUP BY
    Year,
    REPLACE(
        REPLACE(
            REPLACE(
                REPLACE(District, 'Ã¤', 'ae'), 
                'Ã¶', 'oe'
            ), 
            'Ã¼', 'ue'
        ),
        'ÃŸ', 'ss'
    )
ORDER BY
    Year ASC,
    Total_Crimes_Per_District_Year DESC;


-- The most dangerous place in Berlin
SELECT
    location,
    SUM(
        robbery + street_robbery + injury + agg_assault + threat + theft +
        car + from_car + bike + burglary + fire + arson + damage +
        graffiti + drugs + local
    ) AS total_crimes
FROM
    crimes
GROUP BY
    location
ORDER BY
    total_crimes DESC;
    
    
-- The most dangerous place in Berlin per Year
SELECT
    YearlyCrimes.location,

    SUM(CASE WHEN YearlyCrimes.year = 2012 THEN YearlyCrimes.total_crimes ELSE 0 END) AS '2012',
    SUM(CASE WHEN YearlyCrimes.year = 2013 THEN YearlyCrimes.total_crimes ELSE 0 END) AS '2013',
    SUM(CASE WHEN YearlyCrimes.year = 2014 THEN YearlyCrimes.total_crimes ELSE 0 END) AS '2014',
    SUM(CASE WHEN YearlyCrimes.year = 2015 THEN YearlyCrimes.total_crimes ELSE 0 END) AS '2015',
    SUM(CASE WHEN YearlyCrimes.year = 2016 THEN YearlyCrimes.total_crimes ELSE 0 END) AS '2016',
    SUM(CASE WHEN YearlyCrimes.year = 2017 THEN YearlyCrimes.total_crimes ELSE 0 END) AS '2017',
    SUM(CASE WHEN YearlyCrimes.year = 2018 THEN YearlyCrimes.total_crimes ELSE 0 END) AS '2018',
    SUM(CASE WHEN YearlyCrimes.year = 2019 THEN YearlyCrimes.total_crimes ELSE 0 END) AS '2019'  

FROM (
    SELECT
        year,
        location,
        SUM(
            robbery + street_robbery + injury + agg_assault + threat + theft +
            car + from_car + bike + burglary + fire + arson + damage +
            graffiti + drugs + local
        ) AS total_crimes
    FROM
        crimes
    WHERE
        year BETWEEN 2012 AND 2019
    GROUP BY
        year, location
) AS YearlyCrimes
GROUP BY
    YearlyCrimes.location
ORDER BY
SUM(CASE WHEN YearlyCrimes.year = 2019 THEN YearlyCrimes.total_crimes ELSE 0 END) DESC;




-- most common crimes in alexanderplatz in 2019

SELECT
    crime_type,
    SUM(total_count) AS total_count 
FROM (
     --  the Robbery numbers
    SELECT 'robbery' AS crime_type, robbery AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019 -- only want Alexplatz and 2019 data!
    UNION ALL

    --  Street Robbery numbers 
    SELECT 'street_robbery' AS crime_type, street_robbery AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    --  Injury numbers
    SELECT 'injury' AS crime_type, injury AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    --  Aggravated Assault 
    SELECT 'agg_assault' AS crime_type, agg_assault AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    --  Threat numbers
    SELECT 'threat' AS crime_type, threat AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    --  Theft 
    SELECT 'theft' AS crime_type, theft AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    --  Car-related Crimes 
    SELECT 'car' AS crime_type, car AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    -- Theft From Car (separate from 'car' for some reason)
    SELECT 'from_car' AS crime_type, from_car AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    -- Bike Theft
    SELECT 'bike' AS crime_type, bike AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    -- Burglary
    SELECT 'burglary' AS crime_type, burglary AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    -- Fire incidents
    SELECT 'fire' AS crime_type, fire AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    --  Arson
    SELECT 'arson' AS crime_type, arson AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    -- Damage
    SELECT 'damage' AS crime_type, damage AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    -- Graffiti
    SELECT 'graffiti' AS crime_type, graffiti AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    -- drugs Crimes
    SELECT 'drugs' AS crime_type, drugs AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
    UNION ALL

    -- Local Crimes
    SELECT 'local' AS crime_type, local AS total_count
    FROM crimes
    WHERE location = 'alexanderplatz' AND year = 2019
) AS UnpivotedCrimes 
GROUP BY
    crime_type
ORDER BY
    total_count DESC;
    
    
    -- Hypothesis 4 verification: drug crimes in younger neighbourhoods
WITH AggregatedPopulation AS (
    SELECT
        district,
        SUM(total) AS total_pop,
        SUM(age_18_to_27) AS age_18_27_pop
    FROM
        population
    GROUP BY
        district
    HAVING
        SUM(total) > 10000
)
SELECT
    ap.district,
    ap.total_pop AS District_Population,
    ap.age_18_27_pop AS Age_18_27_Total,
    ROUND(
        (CAST(ap.age_18_27_pop AS REAL) / ap.total_pop) * 100, 
        2
    ) AS Age_18_27_Proportion_Percent,
    SUM(c.drugs) AS Total_Drugs_Offenses,
    ROUND(
        (CAST(SUM(c.drugs) AS REAL) / NULLIF(ap.total_pop, 0)) * 1000, 
        2
    ) AS Drugs_Rate_Per_1K_Total_Pop

FROM
    AggregatedPopulation ap
JOIN
    crimes c ON ap.district = c.district

GROUP BY
    ap.district, ap.total_pop, ap.age_18_27_pop
ORDER BY
    Drugs_Rate_Per_1K_Total_Pop DESC;
    
    
    
    -- hypothesis 5 verification, car theft decline over time
    WITH YearlyCrimeData AS (
    SELECT
        year,
        SUM(car) AS Total_Car_Offenses
    FROM
        crimes
    GROUP BY
        year
),
TotalPopulation AS (
    SELECT
        SUM(total) AS Overall_Total_Population
    FROM
        population
)
SELECT
    ycd.year,
    ycd.Total_Car_Offenses,
    tp.Overall_Total_Population,
    (CAST(ycd.Total_Car_Offenses AS REAL) / tp.Overall_Total_Population) * 100000 AS Car_Theft_Rate_Per_100K

FROM
    YearlyCrimeData ycd
CROSS JOIN 
    TotalPopulation tp
ORDER BY
    ycd.year;