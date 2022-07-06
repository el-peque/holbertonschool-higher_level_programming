-- displays the average temperature (Fahrenheit) by city ordered by temperature
SELECT city, AVG(value) as temperature from temperatures GROUP BY city ORDER BY
temperature DESC;
