----------------------------------------DESCRIPCION DEL PROYECTO-------------------------------------------------------

En este proyecto analizamos y preprocesamos un dataset de peliculas, y luego aplicamos machine learning para recomendar peliculas parecidas a una que le mostremos al modelo. 
Se usaron estos datasets https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5

----------------------------------------------CONTENIDOS---------------------------------------------------------------

TRANSFORMACION: Se hizo un preprocesamiento de los datos en el archivo data_transformation.ipynb, en donde se recortaron las columnas mencionadas, se borraron datos nulos, y se crearon las columnas de release_year y return, calculando esta ultima.
Tambien en el archivo cut_transformation se recortaron datos de las bases de datos para hacerlas menos pesadas, borrando datos vacios o peliculas viejas.

EXPLORACION DE DATOS: se hicieron unas visualizacion de algunos datos y sus interacciones en el archivo EDA.ipynb. Se identificaron los años con mas peliculas estrenadas, las peliculas mas populares y la cantidad de peliculas con sus respectivos means de votos.

CREACION DE API: en el archivo main.py se creo la base de la api, con funciones para ver los votos de una pelicula, para ver su score, acceder a todas las peliculas que salieron un dia de la semana, y de un mes.