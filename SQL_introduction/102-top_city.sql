-- Displays the top 3 cities based on temperatures
SELECT city, MAX(value) AS max_temp
FROM temperatures
WHERE month IN (7, 8)  -- Use 'month' instead of 'date'
GROUP BY city
ORDER BY max_temp DESC
LIMIT 3;
