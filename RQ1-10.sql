USE airbnb_project;

SELECT COUNT(*) AS total_listings
FROM airbnb_listings;

-- RQ1
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low Rating'
        WHEN Rating < 4.8 THEN 'Average Rating'
        ELSE 'High Rating'
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
        WHEN 'High Rating' THEN 1
        WHEN 'Average Rating' THEN 2
        WHEN 'Low Rating' THEN 3
    END;

-- RQ2 
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low Rating'
        WHEN Rating >= 4.8 THEN 'High Rating'
    END AS rating_category,

    COUNT(*) AS number_of_listings,

    ROUND(AVG(`Price(in dollar)`), 2) AS average_price,

    ROUND(MIN(`Price(in dollar)`), 2) AS minimum_price,

    ROUND(MAX(`Price(in dollar)`), 2) AS maximum_price

FROM airbnb_listings

WHERE Rating < 4.5
   OR Rating >= 4.8

GROUP BY rating_category;

SELECT
    ROUND(
        AVG(
            CASE
                WHEN Rating >= 4.8
                THEN `Price(in dollar)`
            END
        )
        -
        AVG(
            CASE
                WHEN Rating < 4.5
                THEN `Price(in dollar)`
            END
        ),
        2
    ) AS average_price_difference

FROM airbnb_listings;

-- RQ3
SELECT
    `Property Type`,

    COUNT(*) AS total_listings,

    SUM(
        CASE
            WHEN Rating < 4.5 THEN 1
            ELSE 0
        END
    ) AS poorly_rated_listings,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN Rating < 4.5 THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS poor_rating_percentage

FROM airbnb_listings

GROUP BY `Property Type`

ORDER BY poor_rating_percentage DESC;

-- RQ4
SELECT
    `Amenity Count`,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(`Price(in dollar)`),
        2
    ) AS average_price,

    ROUND(
        MIN(`Price(in dollar)`),
        2
    ) AS minimum_price,

    ROUND(
        MAX(`Price(in dollar)`),
        2
    ) AS maximum_price

FROM airbnb_listings

GROUP BY `Amenity Count`

ORDER BY `Amenity Count`;

-- listings with few amenities
SELECT
    CASE
        WHEN `Amenity Count` <= 2 THEN '0 to 2 Amenities'
        WHEN `Amenity Count` <= 5 THEN '3 to 5 Amenities'
        ELSE '6 or More Amenities'
    END AS amenity_group,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(`Price(in dollar)`),
        2
    ) AS average_price

FROM airbnb_listings

GROUP BY amenity_group

ORDER BY average_price DESC;

-- RQ5

SELECT
    `Amenity Count`,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(Rating),
        3
    ) AS average_rating

FROM airbnb_listings

GROUP BY `Amenity Count`

ORDER BY `Amenity Count`;

-- 
SELECT
    CASE
        WHEN `Amenity Count` <= 2 THEN '0 to 2 Amenities'
        WHEN `Amenity Count` <= 5 THEN '3 to 5 Amenities'
        ELSE '6 or More Amenities'
    END AS amenity_group,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(Rating),
        3
    ) AS average_rating

FROM airbnb_listings

GROUP BY amenity_group

ORDER BY average_rating DESC;

-- RQ6

SELECT
    Country,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(Rating),
        3
    ) AS average_rating,

    ROUND(
        MIN(Rating),
        2
    ) AS minimum_rating,

    ROUND(
        MAX(Rating),
        2
    ) AS maximum_rating

FROM airbnb_listings

GROUP BY Country

ORDER BY average_rating DESC;

-- city
SELECT
    City,
    Country,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(Rating),
        3
    ) AS average_rating

FROM airbnb_listings

GROUP BY City, Country

ORDER BY average_rating DESC;

-- RQ7
SELECT
    Country,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(`Price(in dollar)`),
        2
    ) AS average_price,

    ROUND(
        MIN(`Price(in dollar)`),
        2
    ) AS minimum_price,

    ROUND(
        MAX(`Price(in dollar)`),
        2
    ) AS maximum_price

FROM airbnb_listings

GROUP BY Country

ORDER BY average_price DESC;

-- city level comparisson
SELECT
    City,
    Country,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(`Price(in dollar)`),
        2
    ) AS average_price

FROM airbnb_listings

GROUP BY City, Country

ORDER BY average_price DESC;

-- RQ8
SELECT
    CASE
        WHEN `Number of Reviews` < 50
            THEN 'Under 50 Reviews'

        WHEN `Number of Reviews` < 100
            THEN '50 to 99 Reviews'

        WHEN `Number of Reviews` < 200
            THEN '100 to 199 Reviews'

        ELSE '200 or More Reviews'
    END AS review_group,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(Rating),
        3
    ) AS average_rating,

    ROUND(
        AVG(`Number of Reviews`),
        2
    ) AS average_reviews

FROM airbnb_listings

GROUP BY review_group

ORDER BY average_reviews;

-- RQ9

SELECT
    Month,

    COUNT(*) AS number_of_listings,

    SUM(`Number of Reviews`) AS total_reviews,

    ROUND(
        AVG(`Number of Reviews`),
        2
    ) AS average_reviews,

    ROUND(
        AVG(Rating),
        3
    ) AS average_rating

FROM airbnb_listings

GROUP BY Month

ORDER BY total_reviews DESC;

-- month with most reviews
SELECT
    Month,
    SUM(`Number of Reviews`) AS total_reviews

FROM airbnb_listings

GROUP BY Month

ORDER BY total_reviews DESC

LIMIT 5;

-- Highest average rating
SELECT
    Month,

    ROUND(
        AVG(Rating),
        3
    ) AS average_rating

FROM airbnb_listings

GROUP BY Month

ORDER BY average_rating DESC

LIMIT 5;

-- RQ10
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low Rating'
        WHEN Rating >= 4.8 THEN 'High Rating'
    END AS rating_category,

    COUNT(*) AS number_of_listings,

    ROUND(
        AVG(`Price(in dollar)`),
        2
    ) AS average_price,

    ROUND(
        AVG(`Number of Reviews`),
        2
    ) AS average_reviews,

    ROUND(
        AVG(`Amenity Count`),
        2
    ) AS average_amenities,

    ROUND(
        AVG(Rating),
        3
    ) AS average_rating

FROM airbnb_listings

WHERE Rating < 4.5
   OR Rating >= 4.8

GROUP BY rating_category;

-- comparisson with individual amenities
SELECT
    CASE
        WHEN Rating < 4.5 THEN 'Low Rating'
        WHEN Rating >= 4.8 THEN 'High Rating'
    END AS rating_category,

    COUNT(*) AS number_of_listings,

    ROUND(AVG(WiFi) * 100, 2) AS wifi_percentage,

    ROUND(AVG(Pool) * 100, 2) AS pool_percentage,

    ROUND(AVG(Sauna) * 100, 2) AS sauna_percentage,

    ROUND(AVG(`Hot Tub`) * 100, 2) AS hot_tub_percentage,

    ROUND(AVG(Fireplace) * 100, 2) AS fireplace_percentage,

    ROUND(AVG(`Wood Stove`) * 100, 2) AS wood_stove_percentage,

    ROUND(AVG(Parking) * 100, 2) AS parking_percentage,

    ROUND(AVG(Kitchen) * 100, 2) AS kitchen_percentage,

    ROUND(AVG(Beach) * 100, 2) AS beach_percentage,

    ROUND(AVG(Waterfront) * 100, 2) AS waterfront_percentage,

    ROUND(AVG(`Sea View`) * 100, 2) AS sea_view_percentage,

    ROUND(AVG(`Mountain View`) * 100, 2) AS mountain_view_percentage

FROM airbnb_listings

WHERE Rating < 4.5
   OR Rating >= 4.8

GROUP BY rating_category;





