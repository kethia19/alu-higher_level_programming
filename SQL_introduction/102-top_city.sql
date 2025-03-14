-- Displays the top 3 cities based on temperatures
SELECT city, MAX(value) AS max_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- Filter for July (7) and August (8)
GROUP BY city
ORDER BY max_temp DESC
LIMIT 3;
