import pprint
from os import system
import pandas as pd
from q_fun import *
from archivos import *


nuevo_varid("4HYB35YLMCRIzQobpWs5yv")

# elementos escenciales | 18.09.2020 | jpi
varid1 = get_varid()
token =  get_token()

# set de artistas por id | 18.09.2020 | jpi
artistas_id = set()
# lista de artistas con info completa | 18.09.2020 | jpi
artistas_info = []
# lista de relaciones entre artistas | 18.09.2020 | jpi
conexiones = []

data = {
    'nodes':[],
    'links':[]
}

main_counter = 0


# Recursive artist funtion | 18.09.2020 | jpi
def buscando_problemas(count:int,artist:dict):

    # Variables globales | 18.09.2020 | jpi
    global artistas_id
    global artistas_info
    global conexiones
    global main_counter

    main_counter += 1
    print(main_counter)

    # Agregar artista individual a la base de datos | 18.09.2020 | jpi
    l = len(artistas_id)
    artistas_id.add(artist['id'])
    if ( len(artistas_id) > l ):
        artistas_info.append(artist)

    # Llamar relaciones | 18.09.2020 | jpi
    related = json.loads(get_relacionados(artist['id'],token))

    # Inicio de la recurción | 18.09.2020 | jpi
    if ( count > 0 ):

        # Recorriendo hijos | 18.09.2020 | jpi
        for i in related['artists']:
            print(f"{artist['name']}->{i['name']}")
            conexiones.append(relacionar(artist['id'],i['id']))
            buscando_problemas(count-1,i)

    else:

        # Recorriendo hijos | 18.09.2020 | jpi
        for i in related['artists']:
            conexiones.append(relacionar(artist['id'],i['id']))


# main function | 18.09.2020 | jpi
def main():
    nivel_recurcion = 2
    initial1 = get_artista(varid1,token)
    artist1 = json.loads(initial1)
    buscando_problemas(nivel_recurcion,artist1)
    mandalo_para_el_json(nivel_recurcion,artistas_id,artistas_info,conexiones,artist1['name'])

if __name__ == '__main__':
    main()
