import pymysql

def conect():
    """
    Crea la conexion a la base de datos
    """

    conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='1234567890',
    database = 'streaming_platforms'
    )
    return conn

conn = conect()
cur = conn.cursor()

def query_1(year, platform, time_unit):
    """
    Máxima duración según tipo de film (película/serie), 
    por plataforma y por año: El request debe ser: 
    get_max_duration(año, plataforma, [min o season])
    """

    if time_unit == 'min':
        type_ = 'Movie'
    elif time_unit == 'season':
        type_ = 'TV Show'

    query = """
    SELECT m.Title, max(Duration) as Duration
    FROM Movie m
    JOIN Platform p ON m.IdPlatform = p.IdPlatform
    JOIN Types t ON m.IdType = t.IdType
    WHERE m.ReleaseYear = {} AND p.Platform = '{}' AND t.Type = '{}' AND m.TimeUnit = '{}';
    """.format(year, platform, type_, time_unit)

    cur.execute(query)
    res = cur.fetchall()

    return res


def query_2(platform):
    """
    Cantidad de películas y series (separado) 
    por plataforma El request debe ser: 
    get_count_plataform(plataforma)
    """

    query = """
    SELECT t.Type, count(*)
    FROM Movie m
    JOIN Platform p ON m.IdPlatform = p.IdPlatform
    JOIN Types t ON m.IdType = t.IdType
    WHERE p.Platform = '{}'
    GROUP BY t.Type;
    """.format(platform)

    cur.execute(query)
    res = cur.fetchall()

    return res


def query_3(genr):
    """
    Cantidad de veces que se repite un género y plataforma con mayor 
    frecuencia del mismo. El request debe ser: get_listedin('genero')
    Como ejemplo de género pueden usar 'comedy', el cuál deberia 
    devolverles un cunt de 2099 para la plataforma de amazon.
    """

    query = """
    SELECT a.Platform, max(a.Cantidad)
    FROM (
        SELECT p.Platform, count(*) as Cantidad
        FROM Movie m
        JOIN Platform p ON m.IdPlatform = p.IdPlatform
        JOIN Movie_Genr mg ON m.IdMovie = mg.IdMovie
        JOIN Genr g ON mg.IdGenr = g.IdGenr
        WHERE g.Genr = '{}'
        GROUP BY p.Platform
        ) AS a;
    """.format(genr)

    cur.execute(query)
    res = cur.fetchall()

    return res


def query_4(platform, year):
    """
    Actor que más se repite según plataforma y año. 
    El request debe ser: get_actor(plataforma, año)
    """

    query = """
    SELECT a.Name, count(*) AS Cantidad 
    FROM Movie m
    JOIN Platform p ON m.IdPlatform = p.IdPlatform
    JOIN Movie_Actor ma ON m.IdMovie = ma.IdMovie
    JOIN Actor a ON ma.IdActor = a.IdActor
    WHERE p.Platform = '{}' AND m.ReleaseYear = {} AND a.Name != 'No Info'
    GROUP BY a.Name
    ORDER BY Cantidad DESC
    LIMIT 1;
    """.format(platform, year)

    cur.execute(query)
    res = cur.fetchall()

    return res
