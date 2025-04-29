USE aivshuman; 

#Sectors with higher AI adoption show lower employment growth
#Aggregate AI Adoption by Sector
# Calculate the average AI adoption (obs_value) for each sector across all countries.
SELECT 
    sector,
    AVG(obs_value) AS avg_ai_adoption
FROM country_ai_adoption
GROUP BY sector;

SELECT * FROM occupation_wages;
ALTER TABLE occupation_wages CHANGE naics_title sectors VARCHAR(255);

SELECT * FROM country_ai_adoption;


SELECT 
    ow.sectors,
    AVG(og.employment_percent_change_2023_2033) AS avg_employment_growth
FROM occupation_wages ow
JOIN occupation_growth og ON ow.occupation_code = og.occupation_code
GROUP BY ow.sectors
ORDER BY avg_employment_growth DESC;

SELECT 
    ai.sector,
    ai.avg_ai_adoption,
    eg.avg_employment_growth
FROM
    (SELECT 
        sector,
        AVG(obs_value) AS avg_ai_adoption
     FROM country_ai_adoption
     GROUP BY sectors) ai
JOIN
    (SELECT 
        sectors,
        AVG(employment_percent_change_2023_2033) AS avg_employment_growth
     FROM occupation_growth
     GROUP BY sector) eg
ON ai.sector = eg.sector;

SELECT * FROM ai_job_sentiment;
