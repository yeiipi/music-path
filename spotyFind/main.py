
from sys import argv
import time
import pprint
from os import system
import pandas as pd
from spoty import *
from archivos import *

#si el usuario pone un input de mierda, pailas   |mar sep 29 22:40:00 -05 2020|
if (len(argv) != 3):
    print("USO: python3 {} <nombre del artista> <nivel de recursion>")
    exit()


id_cliente = 'c12d5ca9e15e433298368cbf94a280a4'
secreto_cliente = '1cb6ec606ac048289a3bff4be7895f29'


spotify = SpotApi(id_cliente,secreto_cliente)
artista_perdido = argv[1]


nivel_recurcion = -1
while nivel_recurcion < 0:
    nivel_recurcion = int(argv[2])


# lista de artistas con info completa | 18.09.2020 | jpi
artistas = []
# diccionario principal | 22.09.2020 | jpi
data = { 'nodes':[], 'links':[], 'generos':[]}
# saber cuantas veces se ha intentado crear un nuevo artista | 30.09.2020 | jpi
contando_problemas = 0


# Agrega generos únicos al json | 26.09.2020 | jpi
def agregar_genero(generos:list):

    global data

    if ( len(generos) > 0 ):
        for i in generos:
            if ( i not in data['generos'] ):
                data['generos'].append(i)



# Agrega un link a data.links | 23.09.2020 | jpi
def relacionar(artista1:dict,artista2:dict):

    global artistas
    global data


    data['links'].append(nueva_relación(artista1['id'],artista2['id']))
    agregar_unico(artista1)
    agregar_unico(artista2)



# verificar si el artista ya está en la lista  | 23.09.2020 | jpi
def agregar_unico(art:dict):

    global artistas
    global data
    global contando_problemas


    # verificar que el artista no esté en la base de datos completa | 22.09.2020 | jpi
    try:
        buscando_duplicados = art['id'] not in artistas
    except KeyError:
        raise Exception("agregar_unico():no sirve el id")

    # actualiza la lista con nuevas bandas | 22.09.2020 | jpi
    if ( buscando_duplicados ):
        try:
            data['nodes'].append(nueva_banda(art['id'],art['name'],art['images'][0]['url'],art['popularity'],art['followers']['total'],art['genres']))
            artistas.append(art['id'])
        except IndexError:
            data['nodes'].append(nueva_banda(art['id'],art['name'],"https://www.kindpng.com/picc/m/80-807524_no-profile-hd-png-download.png",art['popularity'],art['followers']['total'],art['genres']))
            artistas.append(art['id'])

    # Agregar generos al json | 26.09.2020 | jpi
    agregar_genero(art['genres'])

    # display cuantos artistas se han intentado crear | 30.09.2020 | jpi
    contando_problemas += 1
    #n = 100   |jue oct  1 13:17:42 -05 2020|
    n = 100
    if ( contando_problemas%n==0 ):
        print(f"Se han hecho {contando_problemas} llamados")



# Recursive artist funtion | 18.09.2020 | jpi
def buscando_problemas(count:int,artist:dict):

    # Variables globales | 18.09.2020 | jpi
    global spotify
    global artistas
    global data


    # Agregar artista individual a la base de datos | 18.09.2020 | jpi
    agregar_unico(artist)

    # Llamar relaciones | 18.09.2020 | jpi
    # related = json.loads(get_relacionados(artist['id'],get_token()))
    related = spotify.obtener_relacionados_id(artist['id'])

    # Inicio de la recurción | 18.09.2020 | jpi
    if ( count > 0 ):

        # Recorriendo hijos | 18.09.2020 | jpi
        try:
            for i in related['artists']:
                relacionar(artist,i)
                buscando_problemas(count-1,i)
        except KeyError:
            raise Exception('buscando_problemas(): error corriendo hijos <if>')
    else:
        # Recorriendo hijos | 18.09.2020 | jpi
        try:
            for i in related['artists']:
                relacionar(artist,i)
        except KeyError:
            raise Exception('buscando_problemas(): error corriendo hijos <else>')


# main function | 18.09.2020 | jpi
def main():

    start = time.time()
    # Variables globales | 28.09.2020 | jpi
    global spotify
    global nivel_recurcion
    global artista_perdido
    global data


    # artist1 = json.loads(initial1)
    art = spotify.obtener_artista_nombre(artista_perdido)
    artist1 = spotify.obtener_artista_id(art['id'])


    print(f"buscando artistas y generando relaciones de {art['name']}...")

    print(f"Se han hecho {contando_problemas} llamados")
    buscando_problemas(nivel_recurcion,artist1)
    print("tarea terminada!!!")
    descripcion =  f"{art['name']}\n"
    descripcion += f"{len(art['name'])*'='}\n"
    descripcion += f"artistas únicos: {len(data['nodes'])} \n"
    descripcion += f"generos únicos: {len(data['generos'])} \n"
    descripcion += f"conexiones unicas: {len(data['links'])}"
    print(descripcion)
    mandalo_para_el_json(nivel_recurcion,data,artist1['name'])
    end = time.time()
    print(f"tiempo:{end-start}")





if __name__ == '__main__':
    main()







