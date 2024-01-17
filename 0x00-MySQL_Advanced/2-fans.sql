-- Title: Number of fans per origin
SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
