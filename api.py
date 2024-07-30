from fastapi import FastAPI, HTTPException
import pandas as pd
app = FastAPI()

data = pd.read_csv('datasets/movies_transformed.csv', index_col=0, parse_dates=["release_date"])

meses = {"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12}
semana = {"lunes":0,"martes":1,"miercoles":2,"jueves":3,"viernes":4,"sabado":5,"domingo":6,}

@app.get("/peliculas_en_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    if  mes.lower() in meses:
        cantidad = data["release_date"].loc[data['release_date'].apply(lambda x : x.month) == meses[mes.lower()]].__len__()

        return str(cantidad) + " peliculas fueron estrenadas en el mes de: " + mes.lower()
    else:
        raise HTTPException(status_code=404, detail="No es un mes")
    
@app.get("/peliculas_en_dia/{dia}")
async def cantidad_filmaciones_dia(dia: str):
    if  dia.lower() in semana:
        cantidad = data["release_date"].loc[data['release_date'].apply(lambda x : x.dayofweek) == semana[dia.lower()]].__len__()

        return str(cantidad) + " peliculas fueron estrenadas en los dias: " + dia.lower()
    else:
        raise HTTPException(status_code=404, detail="No es un dia de la semana")
    
@app.get("/score_titulo/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion: str):
    match = data[data["title"] == titulo_de_la_filmacion]
    if match.__len__() == 0:
        raise HTTPException(status_code=404, detail="No se encontro la pelicula")
    return "La película " + titulo_de_la_filmacion + " fue estrenada en el año " + str(match["release_year"].values[0]) + " con un score de " + str(match["popularity"].values[0])

@app.get("/votos_titulo/{titulo_de_la_filmacion}")
async def votos_titulo(titulo_de_la_filmacion: str):
    match = data[data["title"] == titulo_de_la_filmacion]
    if match.__len__() == 0:
        raise HTTPException(status_code=404, detail="No se encontro la pelicula")
    if match["vote_count"].values[0] < 2000:
        raise HTTPException(status_code=404, detail="La pelicula no fue lo suficientemente valorizada")
    return "La película " + titulo_de_la_filmacion + " fue estrenada en el año " + str(match["release_year"].values[0]) + ". La misma cuenta con un total de  " + str(int(match["vote_count"].values[0])) + " valoraciones, con un promedio de " +  str(match["vote_average"].values[0])

