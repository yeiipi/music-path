

import pprint
from os import system
import pandas as pd
from q_fun import *
from archivos import *

artista_perdido = input("Nombre de la banda o artista que desea buscar:\n> ")
nivel_recurcion = -1
while nivel_recurcion < 0:
    nivel_recurcion = int(input("Niveles de  recurción:\n> "))

nuevo_varid(get_artist_id(artista_perdido))

# elementos escenciales | 18.09.2020 | jpi
varid1 = get_varid()

# lista de artistas con info completa | 18.09.2020 | jpi
artistas = []
# diccionario principal | 22.09.2020 | jpi
data = { 'nodes':[], 'links':[] }


#  | 23.09.2020 | jpi
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


# Recursive artist funtion | 18.09.2020 | jpi
# TODO:terminar nueva forma de relacionar los datos | 22.09.2020 | jpi
def buscando_problemas(count:int,artist:dict):

    # Variables globales | 18.09.2020 | jpi
    global artistas
    global data
    global contando_problemas


    print(f"Artistas: {len(data['nodes'])}")


    # Agregar artista individual a la base de datos | 18.09.2020 | jpi
    agregar_unico(artist)

    # Llamar relaciones | 18.09.2020 | jpi
    related = json.loads(get_relacionados(artist['id'],get_token()))

    # Inicio de la recurción | 18.09.2020 | jpi
    if ( count > 0 ):

        # Recorriendo hijos | 18.09.2020 | jpi
        for i in related['artists']:
            relacionar(artist,i)
            buscando_problemas(count-1,i)
    else:
        # Recorriendo hijos | 18.09.2020 | jpi
        for i in related['artists']:
            relacionar(artist,i)


# main function | 18.09.2020 | jpi
def main():
    global nivel_recurcion
    initial1 = get_artista(varid1,get_token())
    artist1 = json.loads(initial1)
    buscando_problemas(nivel_recurcion,artist1)
    mandalo_para_el_json(nivel_recurcion,data,artist1['name'])

if __name__ == '__main__':
    main()
