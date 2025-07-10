use traficking_victims;

SELECT CEIL(SUM(Nr_of_victims)) AS Total_Victims
FROM Offense;

SELECT 
CEIL(SUM(o.Nr_of_victims)) AS Total_Victims,
c.country_name as country
FROM Offense as o
join country as c
on o.country_id = c.country_id
group by country
order by Total_Victims DESC
limit 20;


SELECT
    c.Country_name,
    CEIL(SUM(o.Nr_of_victims)) AS Total_Victims
FROM
    Offense o
JOIN
    Country c ON o.Country_id = c.Country_id
GROUP BY
    c.Country_name
ORDER BY
    Total_Victims DESC;
    
    
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
    ROUND((CEIL(SUM(o.Nr_of_victims)) / (SELECT SUM(Nr_of_victims) FROM Offense)) * 100, 2) AS Percentage_of_World_Total,
    v.Sex
FROM
    Offense o
JOIN
    Country c ON o.Country_id = c.Country_id
JOIN victim v ON o.victim_id = v.victim_id
GROUP BY
    c.Country_name
ORDER BY
    Total_Victims DESC
LIMIT 10; 
    
    
-- SEX ANALYLIS PER COUNTRY

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
    
    
-- AGE BY SUBREGION   
WITH AgeGroupedVictims AS (
    SELECT
        s.Subregion_name,
        v.Age AS Age_Group,
        COUNT(o.Victim_id) AS Victim_Count
    FROM
        Subregion s
    LEFT JOIN 
        Country c ON s.Subregion_id = c.Subregion_id
    LEFT JOIN 
        Offense o ON c.Country_id = o.Country_id
    LEFT JOIN 
        Victim v ON o.Victim_id = v.Victim_id
    WHERE
        v.Age NOT IN ('Unknown', '')  -- Filter out "Unknown" entries and empty strings, if applicable
    GROUP BY
        s.Subregion_name, v.Age
),
TotalVictims AS (
    SELECT
        s.Subregion_name,
        COUNT(o.Victim_id) AS Total_Victims
    FROM
        Subregion s
    LEFT JOIN 
        Country c ON s.Subregion_id = c.Subregion_id
    LEFT JOIN 
        Offense o ON c.Country_id = o.Country_id
    GROUP BY
        s.Subregion_name
)

SELECT
    agv.Subregion_name,
    agv.Age_Group,
    agv.Victim_Count,
    ROUND((agv.Victim_Count * 100.0 / tv.Total_Victims), 2) AS Percentage
FROM
    AgeGroupedVictims agv
LEFT JOIN
    TotalVictims tv ON agv.Subregion_name = tv.Subregion_name
ORDER BY
    agv.Subregion_name, agv.Age_Group;
    
    

-- AGE ANALYSIS GLOBAL
WITH ExploitationSummary AS (
    SELECT
        o.Category,
        CASE
            WHEN v.Age NOT IN ('Adult', 'Minor') THEN 'Unknown'
            ELSE v.Age
        END AS Age,
        SUM(o.Nr_of_victims) AS Victim_Count
    FROM
        Offense o
    JOIN
        Victim v ON o.Victim_id = v.Victim_id
    WHERE
        o.Dimension = 'by form of exploitation'
    GROUP BY
        o.Category, CASE WHEN v.Age NOT IN ('Adult', 'Minor') THEN 'Unknown' ELSE v.Age END
    HAVING
        Age <> 'Unknown'
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
    es.Age,
    ROUND((es.Victim_Count / tv.Total_Count) * 100, 2) AS Percentage
FROM
    ExploitationSummary es
JOIN
    TotalVictims tv ON es.Category = tv.Category
ORDER BY
    Percentage DESC;