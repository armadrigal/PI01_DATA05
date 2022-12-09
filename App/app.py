from fastapi import FastAPI
import pymysql
import queries

app = FastAPI()

#Presentación
@app.get('/')
def hello():
    return {
        'Titulo: ': 'Proyecto Individual No1',
        'Tema: ': 'Data Engineering',
        'Alumno: ': 'Armando Madrigal Lucatero'
    }

#Consulta 1
@app.get('/get_max_duration')
def get_max_duration(year: str, platform: str, time_unit: str):

    res = queries.query_1(year, platform, time_unit)

    return {
        'Titulo: ': res[0][0], 
        'Duracion: ':res[0][1]
    }

#Consulta 2
@app.get('/get_count_plataform')
def get_count_plataform(platform: str):

    res = queries.query_2(platform)
    
    return {
        'Plataforma: ': platform, 
        'Movie: ': res[0][1], 
        'TV Show: ': res[1][1]
    }

#Consulta 3
@app.get('/get_listedin')
def get_listedin(genr: str):

    res = queries.query_3(genr)

    return {
        'Plataforma: ': res[0][0], 
        'Cantidad: ': res[0][1]
    }

#Consulta 4
@app.get('/get_actor')
def get_actor(platform: str, year: str):
    
    res = queries.query_4(platform, year)

    return {
        'Plataforma: ': platform, 
        'Cantidad: ': res[0][1], 
        'Actor: ': res[0][0]
    }