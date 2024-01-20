-- Title: Number of fans per origin
-- Description: List the number of fans per origin, in descending order.
SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
