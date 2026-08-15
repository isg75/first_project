USE airbnb_project;

SELECT *
FROM airbnb_listings
LIMIT 10;

SELECT
    Country,
    COUNT(*) AS total_properties
FROM airbnb_listings
GROUP BY Country
ORDER BY total_properties DESC;


SELECT
    Country,
    ROUND(AVG(`Price(in dollar)`), 2) AS average_price
FROM airbnb_listings
GROUP BY Country
ORDER BY average_price DESC;
