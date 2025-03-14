-- Displays the top 3 cities based on temperatures
SELECT city, ROUND(AVG(value), 4) AS max_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY max_temp DESC
LIMIT 3;
