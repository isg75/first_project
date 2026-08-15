-- inspect data
SELECT *
FROM airbnb_listings
LIMIT 10;

-- check how many records imported
SELECT COUNT(*) AS total_rows
FROM airbnb_listings;

-- check data structure
DESCRIBE airbnb_listings;

USE airbnb_project;

SHOW TABLES;

SELECT *
FROM airbnb_listings
LIMIT 10;
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low'
        WHEN Rating < 4.8 THEN 'Average'
        ELSE 'High'
    END AS rating_category,
    COUNT(*) AS number_of_listings
FROM airbnb_listings
GROUP BY rating_category
ORDER BY number_of_listings DESC;

-- Group by and order by
SELECT
    Country,
    COUNT(*) AS total_listings,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airbnb_listings
GROUP BY Country
HAVING COUNT(*) >= 5
ORDER BY average_rating DESC
LIMIT 10;

-- Join

SELECT *
FROM location_summary
LIMIT 10;

SELECT
    a.`Property Name`,
    a.Country,
    a.Rating,
    a.`Price(in dollar)` AS listing_price,
    l.location_average_rating,
    l.location_average_price
FROM airbnb_listings AS a
JOIN location_summary AS l
    ON a.Country = l.Country
ORDER BY a.Rating DESC
LIMIT 20;

SELECT
    a.`Property Name`,
    a.`Property Type`,
    a.Country,
    a.Rating,
    a.`Price(in dollar)` AS listing_price,
    l.location_average_rating,
    l.location_average_price
FROM airbnb_listings AS a
JOIN location_summary AS l
    ON a.Country = l.Country
ORDER BY a.Rating DESC
LIMIT 20;

-- Top 20 highest rated listings
SELECT
    CASE
        WHEN rating < 4.5 THEN 'Low'
        WHEN rating < 4.8 THEN 'Average'
        ELSE 'High'
    END AS rating_category,
    COUNT(*) AS number_of_listings,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM airbnb_listings),
        2
    ) AS percentage
FROM airbnb_listings
GROUP BY rating_category;


SELECT
    `Property Name`,
    `Property Type`,
    City,
    Country,
    `Price(in dollar)` AS price,
    Rating,
    `Number of Reviews` AS number_of_reviews,
    `Amenity Count` AS amenity_count,

    CASE
        WHEN Rating < 4.5 THEN 'Low'
        WHEN Rating < 4.8 THEN 'Average'
        ELSE 'High'
    END AS rating_category

FROM airbnb_listings

ORDER BY
    Rating DESC,
    `Number of Reviews` DESC

LIMIT 20;

-- RQ1
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low'
        WHEN Rating < 4.8 THEN 'Average'
        ELSE 'High'
    END AS rating_category,

    COUNT(*) AS number_of_listings,

    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM airbnb_listings),
        2
    ) AS percentage

FROM airbnb_listings

GROUP BY rating_category

ORDER BY
    CASE rating_category
        WHEN 'High' THEN 1
        WHEN 'Average' THEN 2
        WHEN 'Low' THEN 3
    END;
    
    -- Top 20 lowest rated listings:
    
    SELECT
    `Property Name`,
    `Property Type`,
    City,
    Country,
    `Price(in dollar)` AS price,
    Rating,
    `Number of Reviews` AS number_of_reviews,
    `Amenity Count` AS amenity_count

FROM airbnb_listings

WHERE Rating < 4.5

ORDER BY
    Rating ASC,
    `Number of Reviews` DESC

LIMIT 20;

--  20 highest priced listings among the low rated properties
SELECT
    `Property Name`,
    `Property Type`,
    City,
    Country,
    `Price(in dollar)` AS price,
    Rating,
    `Number of Reviews` AS number_of_reviews,
    `Amenity Count` AS amenity_count
FROM airbnb_listings
WHERE Rating < 4.5
ORDER BY `Price(in dollar)` DESC
LIMIT 20;

-- top 10 countries with the highest average ratings
SELECT
    Country,
    COUNT(*) AS total_listings,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airbnb_listings
GROUP BY Country
ORDER BY average_rating DESC
LIMIT 10;

-- top 10 locations with the lowest average ratings
SELECT
    Country,
    COUNT(*) AS total_listings,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airbnb_listings
GROUP BY Country
HAVING COUNT(*) >= 5
ORDER BY average_rating ASC
LIMIT 10;

-- top 10 listings with zero identified amenities but high ratings

SELECT
    `Property Name`,
    `Property Type`,
    City,
    Country,
    `Price(in dollar)` AS price,
    Rating,
    `Number of Reviews` AS number_of_reviews,
    `Amenity Count` AS amenity_count
FROM airbnb_listings
WHERE `Amenity Count` = 0
    AND Rating >= 4.8
ORDER BY
    Rating DESC,
    `Number of Reviews` DESC
LIMIT 10;







-- RQ1. What is the distribution of Airbnb listings based on high, average, and low ratings?
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low'
        WHEN Rating < 4.8 THEN 'Average'
        ELSE 'High'
    END AS rating_category,

    COUNT(*) AS number_of_listings,

    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM airbnb_listings),
        2
    ) AS percentage

FROM airbnb_listings

GROUP BY rating_category

ORDER BY
    CASE rating_category
        WHEN 'High' THEN 1
        WHEN 'Average' THEN 2
        WHEN 'Low' THEN 3
    END;
-- The Airbnb listings are predominantly highly rated. Of the 604 listings, 460 or 76.16% have high ratings of 4.8 or above. Another 124 listings or 20.53% have average ratings, while only 20 listings or 3.31% are classified as low rated. This indicates that poorly rated listings represent a relatively small segment of the dataset.

-- RQ2. Is there a significant difference in price between poorly rated and highly rated Airbnb listings?
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low'
        WHEN Rating >= 4.8 THEN 'High'
    END AS rating_category,
    
    COUNT(*) AS total_listings,
    
    ROUND(
        AVG(`Price(in dollar)`),
        2
    ) AS average_price,
    
    MIN(`Price(in dollar)`) AS minimum_price,
    
    MAX(`Price(in dollar)`) AS maximum_price

FROM airbnb_listings

WHERE Rating < 4.5
   OR Rating >= 4.8

GROUP BY rating_category

ORDER BY average_price DESC;
-- Highly rated listings are significantly more expensive than poorly rated listings, although price should be interpreted as an association with rating rather than a cause of better guest satisfaction.

-- RQ4.  Do amenities significantly influence the price of Airbnb listings
SELECT
    `Amenity Count` AS amenity_count,
    COUNT(*) AS total_listings,
    ROUND(AVG(`Price(in dollar)`), 2) AS average_price,
    ROUND(MIN(`Price(in dollar)`), 2) AS minimum_price,
    ROUND(MAX(`Price(in dollar)`), 2) AS maximum_price
FROM airbnb_listings
GROUP BY `Amenity Count`
ORDER BY amenity_count;

-- Top 10 listings with most number of amenities
SELECT
    `Property Name`,
    `Property Type`,
    City,
    Country,
    `Amenity Count` AS amenity_count,
    `Price(in dollar)` AS price,
    Rating
FROM airbnb_listings
ORDER BY
    `Amenity Count` DESC,
    `Price(in dollar)` DESC
LIMIT 10;
-- Amenities are significantly associated with Airbnb listing prices, but the relationship is weak. Listings with more identified amenities tend to have slightly higher prices, suggesting that amenities may contribute to pricing but are unlikely to be a major pricing factor on their own.

-- RQ5. Do amenities significantly influence Airbnb ratings?
SELECT
    `Amenity Count` AS amenity_count,
    COUNT(*) AS total_listings,
    ROUND(AVG(Rating), 2) AS average_rating,
    ROUND(MIN(Rating), 2) AS minimum_rating,
    ROUND(MAX(Rating), 2) AS maximum_rating
FROM airbnb_listings
GROUP BY `Amenity Count`
ORDER BY `Amenity Count`;

-- compare zero amenities with high ratings
SELECT
    `Property Name`,
    `Property Type`,
    City,
    Country,
    `Amenity Count` AS amenity_count,
    Rating,
    `Number of Reviews` AS number_of_reviews
FROM airbnb_listings
WHERE `Amenity Count` = 0
    AND Rating >= 4.8
ORDER BY
    Rating DESC,
    `Number of Reviews` DESC
LIMIT 10;
-- Amenity count is significantly associated with Airbnb guest ratings. However, the relationship is very weak and negative, with a Spearman correlation of negative 0.115. This indicates that listings with more identified amenities do not necessarily receive higher guest ratings.

-- RQ6. Does the location of an Airbnb listing significantly influence guest ratings?
SELECT
    Country AS location,
    COUNT(*) AS total_listings,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airbnb_listings
GROUP BY Country
HAVING COUNT(*) >= 5
ORDER BY average_rating DESC
LIMIT 10;

-- top 10 location with lowest ratings
SELECT
    Country AS location,
    COUNT(*) AS total_listings,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airbnb_listings
GROUP BY Country
HAVING COUNT(*) >= 5
ORDER BY average_rating ASC
LIMIT 10;
-- Guest ratings differ significantly across Airbnb locations. The Kruskal Wallis test produced a statistically significant result, indicating that rating distributions are not the same across all locations.


-- RQ7. Does the location of an Airbnb listing significantly influence Airbnb prices?
SELECT
    Country AS location,
    COUNT(*) AS total_listings,
    ROUND(AVG(`Price(in dollar)`), 2) AS average_price
FROM airbnb_listings
GROUP BY Country
HAVING COUNT(*) >= 5
ORDER BY average_price DESC
LIMIT 10;

-- top 10 locations with lowest average prices
SELECT
    Country AS location,
    COUNT(*) AS total_listings,
    ROUND(AVG(`Price(in dollar)`), 2) AS average_price
FROM airbnb_listings
GROUP BY Country
HAVING COUNT(*) >= 5
ORDER BY average_price ASC
LIMIT 10;

-- Airbnb listing prices differ significantly across locations. The Kruskal Wallis test provides sufficient statistical evidence to reject the null hypothesis, indicating that price distributions are not the same across all locations.

-- RQ8. Does the number of reviews significantly influence Airbnb ratings?
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low'
        WHEN Rating < 4.8 THEN 'Average'
        ELSE 'High'
    END AS rating_category,
    COUNT(*) AS total_listings,
    ROUND(AVG(`Number of Reviews`), 2) AS average_reviews,
    MIN(`Number of Reviews`) AS minimum_reviews,
    MAX(`Number of Reviews`) AS maximum_reviews
FROM airbnb_listings
GROUP BY rating_category
ORDER BY average_reviews DESC;

-- top 10 most reviewed properties
SELECT
    `Property Name`,
    `Property Type`,
    City,
    Country,
    `Number of Reviews` AS number_of_reviews,
    Rating,
    `Price(in dollar)` AS price
FROM airbnb_listings
ORDER BY `Number of Reviews` DESC
LIMIT 10;
-- The number of reviews is significantly associated with Airbnb guest ratings. However, the relationship is weak and negative, with a Spearman correlation of negative 0.184. Listings with more reviews tend to have slightly lower ratings, but review volume has only a weak relationship with guest ratings.


-- RQ9. Which month has the highest number of reviews and the highest average Airbnb rating?

SELECT
    Month,
    COUNT(*) AS total_listings,
    SUM(`Number of Reviews`) AS total_reviews,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airbnb_listings
GROUP BY Month
ORDER BY total_reviews DESC;

-- Month with highest reviews

SELECT
    Month,
    COUNT(*) AS total_listings,
    SUM(`Number of Reviews`) AS total_reviews
FROM airbnb_listings
GROUP BY Month
ORDER BY total_reviews DESC
LIMIT 1;

-- month with the highest average rating 
SELECT
    Month,
    COUNT(*) AS total_listings,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airbnb_listings
GROUP BY Month
ORDER BY average_rating DESC
LIMIT 1;

SELECT
    Month,
    COUNT(*) AS total_listings,
    SUM(`Number of Reviews`) AS total_reviews,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airbnb_listings
GROUP BY Month
HAVING COUNT(*) >= 5
ORDER BY average_rating DESC;
-- June has the highest aggregated number of reviews, with 66,386 reviews. May has the highest average rating at 4.98, but this result is based on only one listing and therefore should not be considered representative of overall monthly performance.

-- RQ10. What improvements should Airbnb hosts prioritize to transform poorly rated listings into highly rated listings into highly rated accommodations?
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low'
        WHEN Rating >= 4.8 THEN 'High'
    END AS rating_category,

    COUNT(*) AS total_listings,

    ROUND(AVG(`Price(in dollar)`), 2) AS average_price,

    ROUND(AVG(`Number of Reviews`), 2) AS average_reviews,

    ROUND(AVG(`Amenity Count`), 2) AS average_amenities

FROM airbnb_listings

WHERE Rating < 4.5
   OR Rating >= 4.8

GROUP BY rating_category;

-- Airbnb hosts should prioritize the overall quality and value of the guest experience rather than simply increasing the number of amenities. The analysis shows that amenities have only a weak relationship with price and ratings, while location, property type, and pricing patterns are significantly associated with listing performance. Hosts should therefore focus on appropriate local market pricing, property and service quality, useful and well maintained amenities, accurate guest expectations, and continuous monitoring of guest feedback.

-- Recommended priorities
-- Improve the overall guest experience. Since amenity count has only a very weak relationship with ratings, hosts should prioritize the quality and consistency of the stay rather than simply adding more amenities.
-- Focus on value for money. Highly rated listings are significantly more expensive in your dataset, but hosts should ensure that the property's quality and experience justify its price.
-- Benchmark against the local market. Because both prices and ratings differ significantly by location, hosts should compare themselves with similar listings in the same geographic market.
-- Benchmark against the same property type. Hotels, hotel rooms, lofts, apartments, and other property types have different rating patterns. Hosts should compare performance with directly comparable accommodations.
-- Prioritize useful amenities over quantity. More amenities do not automatically produce better ratings. Hosts should focus on amenities that are functional, relevant, and properly maintained.
-- Monitor guest feedback continuously. Review volume alone does not strongly explain ratings, but recurring complaints can help identify specific service or property issues that require attention.



