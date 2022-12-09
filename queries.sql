USE streaming_platforms;

-- Consulta 1:

SELECT m.Title, max(Duration) as Duration
FROM Movie m
JOIN Platform p ON m.IdPlatform = p.IdPlatform
JOIN Types t ON m.IdType = t.IdType
WHERE m.ReleaseYear = 2018 AND p.Platform = 'Hulu' AND t.Type = 'Movie' AND m.TimeUnit = 'min';


-- Consulta 2:

SELECT t.Type, count(*)
FROM Movie m
JOIN Platform p ON m.IdPlatform = p.IdPlatform
JOIN Types t ON m.IdType = t.IdType
WHERE p.Platform = 'Netflix'
GROUP BY t.Type;


-- Consulta 3:

SELECT a.Platform, max(a.Cantidad)
FROM (
	SELECT p.Platform, count(*) as Cantidad
	FROM Movie m
	JOIN Platform p ON m.IdPlatform = p.IdPlatform
	JOIN Movie_Genr mg ON m.IdMovie = mg.IdMovie
	JOIN Genr g ON mg.IdGenr = g.IdGenr
	WHERE g.Genr = 'Comedy'
	GROUP BY p.Platform
	) AS a;


-- Consulta 4:

SELECT a.Name, count(*) AS Cantidad
FROM Movie m
JOIN Platform p ON m.IdPlatform = p.IdPlatform
JOIN Movie_Actor ma ON m.IdMovie = ma.IdMovie
JOIN Actor a ON ma.IdActor = a.IdActor
WHERE p.Platform = 'Netflix' AND m.ReleaseYear = 2018 AND a.Name != 'No Info'
GROUP BY a.Name
ORDER BY Cantidad DESC
LIMIT 1;
