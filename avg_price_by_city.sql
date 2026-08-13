USE CrossDataHosts;

SELECT *
FROM listing;

SELECT *
FROM locations;

SELECT *
FROM offers;

SELECT *
FROM property;



SELECT loc.city, ROUND(AVG(o.price)) as avg_price, ROUND(AVG(lis.rating_value)) AS avg_rating
FROM locations AS loc
JOIN listing AS lis
ON loc.location_id = lis.location_id
JOIN offers as o
ON lis.listing_id = o.listing_id
WHERE loc.country = "US"
GROUP BY loc.city
ORDER BY avg_price DESC
LIMIT 5;

