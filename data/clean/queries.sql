USE traficking_victims;

SELECT CEIL(SUM(Nr_of_victims)) AS Total_Victims
FROM Offense;

-- TOTAL VICTIMS WORLD WIDE TOP 10 
SELECT
    c.Country_name,
    CEIL(SUM(o.Nr_of_victims)) AS Total_Victims,
    ROUND((CEIL(SUM(o.Nr_of_victims)) / (SELECT SUM(Nr_of_victims) FROM Offense)) * 100, 2) AS Percentage_of_World_Total
FROM
    Offense o
JOIN
    Country c ON o.Country_id = c.Country_id
GROUP BY
    c.Country_name
ORDER BY
    Total_Victims DESC
LIMIT 10;

-- Amount female / male victims per country
SELECT
    c.Country_name,
    CEIL(SUM(o.Nr_of_victims)) AS Total_Victims,
    CEIL(SUM(CASE WHEN v.Sex = 'Female' THEN o.Nr_of_victims ELSE 0 END)) AS Female_Victims_Count,
    CEIL(SUM(CASE WHEN v.Sex = 'Male' THEN o.Nr_of_victims ELSE 0 END)) AS Male_Victims_Count,
    CEIL(SUM(CASE WHEN v.Sex NOT IN ('Male', 'Female') OR v.Sex IS NULL THEN o.Nr_of_victims ELSE 0 END)) AS Unknown_Sex_Victims_Count
FROM
    Offense o
JOIN
    Country c ON o.Country_id = c.Country_id
JOIN
    Victim v ON o.Victim_id = v.Victim_id
GROUP BY
    c.Country_name
ORDER BY
    Total_Victims DESC
LIMIT 10;



-- SEX PERCENTAGES PER COUNTRY
SELECT
    c.Country_name,
    CEIL(SUM(o.Nr_of_victims)) AS Total_Victims,
    
    ROUND(
        100 * SUM(CASE WHEN v.Sex = 'Female' THEN o.Nr_of_victims ELSE 0 END) 
        / NULLIF(SUM(o.Nr_of_victims), 0), 2
    ) AS Female_Percentage,

    ROUND(
        100 * SUM(CASE WHEN v.Sex = 'Male' THEN o.Nr_of_victims ELSE 0 END) 
        / NULLIF(SUM(o.Nr_of_victims), 0), 2
    ) AS Male_Percentage,

    ROUND(
        100 * SUM(CASE WHEN v.Sex NOT IN ('Male', 'Female') OR v.Sex IS NULL THEN o.Nr_of_victims ELSE 0 END) 
        / NULLIF(SUM(o.Nr_of_victims), 0), 2
    ) AS Unknown_Sex_Percentage

FROM
    Offense o
JOIN
    Country c ON o.Country_id = c.Country_id
JOIN
    Victim v ON o.Victim_id = v.Victim_id
GROUP BY
    c.Country_name
ORDER BY
    Total_Victims DESC
LIMIT 10;

-- SEX GLOBALLY 
SELECT
    CASE
        WHEN v.Sex IS NULL OR v.Sex NOT IN ('Male', 'Female') THEN 'Unknown'
        ELSE v.Sex
    END AS Sex,
    CEIL(SUM(o.Nr_of_victims)) AS Victim_Count,
    ROUND(
        100 * SUM(o.Nr_of_victims) / (
            SELECT SUM(Nr_of_victims) FROM Offense
        ),
        2
    ) AS Global_Percentage
FROM
    Offense o
JOIN
    Victim v ON o.Victim_id = v.Victim_id
GROUP BY
    CASE
        WHEN v.Sex IS NULL OR v.Sex NOT IN ('Male', 'Female') THEN 'Unknown'
        ELSE v.Sex
    END
ORDER BY
    Victim_Count DESC;



-- Victim Count by Category and Sex (Top 10 Categories Globally)
SELECT
    c.Country_name,
    o.Category,
    CASE
        WHEN v.Sex IS NULL OR v.Sex NOT IN ('Male', 'Female') THEN 'Unknown'
        ELSE v.Sex
    END AS Sex,
    CEIL(SUM(o.Nr_of_victims)) AS Victim_Count,
    CEIL(SUM(SUM(o.Nr_of_victims)) OVER (PARTITION BY c.Country_name)) AS Country_Total_Victims
FROM
    Offense o
JOIN
    Country c ON o.Country_id = c.Country_id
JOIN
    Victim v ON o.Victim_id = v.Victim_id
GROUP BY
    c.Country_name,
    o.Category,
    CASE
        WHEN v.Sex IS NULL OR v.Sex NOT IN ('Male', 'Female') THEN 'Unknown'
        ELSE v.Sex
    END
ORDER BY
    Country_Total_Victims DESC,
    c.Country_name,
    o.Category,
    Sex;

-- UNIQUE VALES OF DIMENSIN IN offense TABLE -- DON'T USE
SELECT
    c.Country_name,
    o.Category,
    CASE
        WHEN v.Sex IS NULL OR v.Sex NOT IN ('Male', 'Female') THEN 'Unknown'
        ELSE v.Sex
    END AS Sex,
    CEIL(SUM(o.Nr_of_victims)) AS Victim_Count,
    CEIL(SUM(SUM(o.Nr_of_victims)) OVER (PARTITION BY c.Country_name)) AS Country_Total_Victims
FROM
    Offense o
JOIN
    Country c ON o.Country_id = c.Country_id
JOIN
    Victim v ON o.Victim_id = v.Victim_id
GROUP BY
    c.Country_name,
    o.Category,
    o.Dimension,  -- Used in grouping, but not selected
    CASE
        WHEN v.Sex IS NULL OR v.Sex NOT IN ('Male', 'Female') THEN 'Unknown'
        ELSE v.Sex
    END
ORDER BY
    Country_Total_Victims DESC,
    Victim_Count DESC,
    c.Country_name,
    o.Category,
    Sex;


-- next try UNIQUE VALES OF DIMENSIN IN offense TABLE
SELECT
    c.Country_name,
    o.Category,
    CEIL(SUM(o.Nr_of_victims)) AS Victim_Count,
    CEIL(SUM(SUM(o.Nr_of_victims)) OVER (PARTITION BY c.Country_name)) AS Country_Total_Victims
FROM
    Offense o
JOIN
    Country c ON o.Country_id = c.Country_id
JOIN
    Victim v ON o.Victim_id = v.Victim_id
GROUP BY
    c.Country_name,
    o.Category,
    o.Dimension  -- Keep for internal grouping
ORDER BY
    Country_Total_Victims DESC,
    Victim_Count DESC,
    c.Country_name,
    o.Category;


-- GLOBAL TYPE OF CRIME
SELECT
    o.Category,
    CEIL(SUM(o.Nr_of_victims)) AS Victim_Count,
    CEIL(SUM(SUM(o.Nr_of_victims)) OVER ()) AS Global_Total_Victims
FROM
    Offense o
JOIN
    Victim v ON o.Victim_id = v.Victim_id
GROUP BY
    o.Category,
    o.Dimension  -- Group by Dimension to keep categories separate across types
ORDER BY
    Victim_Count DESC,
    o.Category;

-- top 4 countries %age per type per crime
SELECT
    o.Category,
    ROUND(100 * SUM(o.Nr_of_victims) / SUM(SUM(o.Nr_of_victims)) OVER (), 2) AS Percentage_of_Global
FROM
    Offense o
JOIN
    Victim v ON o.Victim_id = v.Victim_id
GROUP BY
    o.Category,
    o.Dimension
ORDER BY
    SUM(o.Nr_of_victims) DESC
LIMIT 4;


-- AGE Separation according to the top 4 countries
WITH TopCountries AS (
    SELECT
        o.Country_id
    FROM
        Offense o
    GROUP BY
        o.Country_id
    ORDER BY
        SUM(o.Nr_of_victims) DESC
    LIMIT 4
),
AgeGrouped AS (
    SELECT
        c.Country_name,
        o.Category,
        CASE
            WHEN v.Age IS NULL OR v.Age NOT REGEXP '^[0-9]+$' THEN 'Unknown'
            WHEN CAST(v.Age AS UNSIGNED) < 18 THEN 'Minor'
            ELSE 'Adult'
        END AS Age_Group,
        SUM(o.Nr_of_victims) AS Victim_Count
    FROM
        Offense o
    JOIN
        Country c ON o.Country_id = c.Country_id
    JOIN
        Victim v ON o.Victim_id = v.Victim_id
    WHERE
        o.Country_id IN (SELECT Country_id FROM TopCountries)
    GROUP BY
        c.Country_name,
        o.Category,
        Age_Group
)
SELECT *
FROM AgeGrouped
ORDER BY
    Country_name,
    Category,
    FIELD(Age_Group, 'Minor', 'Adult', 'Unknown');

-- SEX ANALYSIS

WITH VictimTotals AS (
    SELECT
        c.Country_name,
        o.Category,
        v.Sex,
        SUM(o.Nr_of_victims) AS Victim_Count
    FROM
        Offense o
    JOIN
        Country c ON o.Country_id = c.Country_id
    JOIN
        Victim v ON o.Victim_id = v.Victim_id
    WHERE
        o.Dimension = 'by form of exploitation'
        AND v.Sex IN ('Male', 'Female')
    GROUP BY
        c.Country_name, o.Category, v.Sex
),
TotalVictims AS (
    SELECT
        c.Country_name,
        o.Category,
        SUM(o.Nr_of_victims) AS Total_Count
    FROM
        Offense o
    JOIN
        Country c ON o.Country_id = c.Country_id
    WHERE
        o.Dimension = 'by form of exploitation'
    GROUP BY
        c.Country_name, o.Category
)
SELECT
    vt.Country_name,
    vt.Category,
    vt.Sex,
    vt.Victim_Count,
    ROUND((vt.Victim_Count / tv.Total_Count) * 100, 2) AS Percentage
FROM
    VictimTotals vt
JOIN
    TotalVictims tv ON vt.Country_name = tv.Country_name
                   AND vt.Category = tv.Category
ORDER BY
    vt.Victim_Count DESC, tv.Country_name, tv.Category
LIMIT 10;


-- SEX ANALYLIS GLOBAL
WITH ExploitationSummary AS (
    SELECT
        o.Category,
        CASE
            WHEN v.Sex NOT IN ('Male', 'Female') THEN 'Unknown'
            ELSE v.Sex
        END AS Sex,
        SUM(o.Nr_of_victims) AS Victim_Count
    FROM
        Offense o
    JOIN
        Victim v ON o.Victim_id = v.Victim_id
    WHERE
        o.Dimension = 'by form of exploitation'
    GROUP BY
        o.Category, CASE WHEN v.Sex NOT IN ('Male', 'Female') THEN 'Unknown' ELSE v.Sex END
    HAVING
        Sex <> 'Unknown'
),
TotalVictims AS (
    SELECT
        o.Category,
        SUM(o.Nr_of_victims) AS Total_Count
    FROM
        Offense o
    WHERE
        o.Dimension = 'by form of exploitation'
    GROUP BY
        o.Category
)
SELECT
    es.Category,
    es.Sex,
    ROUND((es.Victim_Count / tv.Total_Count) * 100, 2) AS Percentage
FROM
    ExploitationSummary es
JOIN
    TotalVictims tv ON es.Category = tv.Category
ORDER BY
    Percentage DESC;


-- XX
WITH RankedCountries AS (
    SELECT
        o.Country_id,
        c.Country_name,
        SUM(o.Nr_of_victims) AS Total_Victims
    FROM
        Offense o
    JOIN
        Country c ON o.Country_id = c.Country_id
    GROUP BY
        o.Country_id, c.Country_name
    ORDER BY
        Total_Victims DESC
    LIMIT 4
)

SELECT
    rc.Country_name,
    sq.Category,
    sq.Age_Group,
    CONCAT(rc.Country_name, ' - ', sq.Age_Group) AS Country_Age_Label,
    SUM(sq.Nr_of_victims) AS Victim_Count
FROM (
    SELECT
        o.Country_id,
        o.Category,
        CASE
            WHEN v.Age IS NULL OR v.Age NOT REGEXP '^[0-9]+$' THEN 'Unknown'
            WHEN CAST(v.Age AS UNSIGNED) < 18 THEN 'Minor'
            ELSE 'Adult'
        END AS Age_Group,
        o.Nr_of_victims
    FROM
        Offense o
    JOIN
        Victim v ON o.Victim_id = v.Victim_id
    JOIN
        RankedCountries rc ON o.Country_id = rc.Country_id
) AS sq
JOIN
    Country rc ON sq.Country_id = rc.Country_id
GROUP BY
    rc.Country_name,
    sq.Category,
    sq.Age_Group
ORDER BY
    rc.Country_name,
    sq.Category,
    FIELD(sq.Age_Group, 'Minor', 'Adult', 'Unknown');
