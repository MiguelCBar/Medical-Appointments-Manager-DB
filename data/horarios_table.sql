DROP TABLE IF EXISTS Horarios;

CREATE TABLE Horarios (
    data DATE NOT NULL,
    hora TIME NOT NULL,
    PRIMARY KEY(data, hora)
);

WITH NearestInterval AS (
    SELECT
        CASE
            WHEN EXTRACT(MINUTE FROM CURRENT_TIMESTAMP) < 30 THEN
                date_trunc('hour', CURRENT_TIMESTAMP) + interval '1hour' + interval '30 minutes'
            ELSE
                date_trunc('hour', CURRENT_TIMESTAMP) + interval '2 hour'
        END AS start_time
),
GeneratedHorarios AS (
    SELECT 
        gs.datahora::date AS data, 
        gs.datahora::time AS hora
    FROM 
        generate_series(
            (SELECT start_time FROM NearestInterval),
            '2024-12-31 23:59:59'::timestamp, 
            interval '30 minutes'
        ) AS gs(datahora)
    WHERE
        (EXTRACT(HOUR FROM gs.datahora) BETWEEN 8 AND 12
        OR EXTRACT(HOUR FROM gs.datahora) BETWEEN 14 AND 18)
        AND (EXTRACT(MINUTE FROM gs.datahora) = 0 OR EXTRACT(MINUTE FROM gs.datahora) = 30)
        AND ((EXTRACT(MONTH FROM gs.datahora) = 2 AND EXTRACT(DAY FROM gs.datahora) <= 29) OR
            (EXTRACT(MONTH FROM gs.datahora) IN (4, 6, 9, 11) 
            AND EXTRACT(DAY FROM gs.datahora) <= 30) OR
            (EXTRACT(MONTH FROM gs.datahora) IN (1, 3, 5, 7, 8, 10, 12)
            AND EXTRACT(DAY FROM gs.datahora) <= 31)
            )
)
INSERT INTO Horarios (data, hora)
SELECT data, hora 
FROM GeneratedHorarios;

