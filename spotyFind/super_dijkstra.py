import networkx as nx
import json
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import time
import pprint
from os import system
import pandas as pd
from spoty import *
from archivos import *
import urllib.parse
import requests
from bs4 import BeautifulSoup
from youtubesearchpython import SearchVideos
from os import popen

path = "../relaciones/bandas_colombianas.json"

if((len(argv)== 4) or (len(argv) == 3)):
    def get_nombre_banda(id_banda):
        for i in datos['nodes']:
            if(i['id'] == id_banda):
                return(i['nombre'])
            else:
                pass
        return("no se encontro")

    with open (path) as json_file:
        datos = json.load(json_file)

    id_cliente = 'c12d5ca9e15e433298368cbf94a280a4'
    secreto_cliente = '1cb6ec606ac048289a3bff4be7895f29'
    spotify = SpotApi(id_cliente,secreto_cliente)

#agarro el artista1   |mar oct 27 22:37:51 -05 2020|
    artista_perdido1 = argv[1]
    art1 = spotify.obtener_artista_nombre(artista_perdido1)
    artist1 = spotify.obtener_artista_id(art1['id'])

#agarro el artista2   |mar oct 27 22:37:56 -05 2020|
    artista_perdido2 = argv[2]
    art2 = spotify.obtener_artista_nombre(artista_perdido2)
    artist2 = spotify.obtener_artista_id(art2['id'])




    tuplas = []
    for i in datos['links']:
        source = i['source']
        target = i['target']
        tuplas.append((source,target))

    G = nx.Graph()
    G.add_edges_from(tuplas)

    try:
        chaman_shortest_path = nx.shortest_path( G , artist1['id'],artist2['id'])
        lista_nombres = []
        for i in chaman_shortest_path:
            nombre = get_nombre_banda(i)
            lista_nombres.append(nombre)
        print("Resultado de Dijkstra entre las bandas:")
        cont = 1
        for i in lista_nombres:
            print(cont , i)
            cont += 1
    except:
        print("no se puede hacer dikstra entre esas dos bandas, puede que una de las dos no esté en los datos")
        exit()


            #Parte grafica:   |mar oct 27 22:20:20 -05 2020|

    #pos = nx.spring_layout(G)  # positions for all nodes
    #nx.draw_networkx(G, pos , node_color = "r"  )
    #plt.show()
    #nx.draw_networkx(G, pos , node_color = "r" , nodelist = chaman_shortest_path)
    #plt.show()



            #Aca toca hacer el bot que arme la playlist   |mar oct 27 23:31:27 -05 2020|
    print('\n')


    if(len(argv) == 4):
        nombres_canciones = []
        cantidad_temazos_por_artista = int(argv[3])
        playlist = []
        cont = 1

        print("Temas:")
        for i in lista_nombres:
            search = SearchVideos(i , offset = 1, mode = "json", max_results = cantidad_temazos_por_artista)
            videos = search.result()
            videos = json.loads(search.result())
            for j in videos['search_result']:
                #se pueden agarrar mas atributos como el id,canal,numero de views, duracion... y las fotos   |mié oct 28 00:39:36 -05 2020|
                titulo_tema = j['title']
                nombres_canciones.append(titulo_tema)
                link_tema = j['link']
                print("{}:".format(cont),titulo_tema)
                playlist.append(link_tema)
                cont += 1


        print('\n'*2)

                    #Ahora descargo la playlist   |mié oct 28 00:41:09 -05 2020|
                    #La descarga de la playlist funciona, sin embargo, en mi computador youtube-dl tiene fallos   |mié oct 28 02:59:27 -05 2020|

        #       CREAR LA PLAYLIST   |mié oct 28 02:58:16 -05 2020|
        #folder_name #="../playlists/playlist_from_{}_to_{}".format(argv[1].replace(" ","") , argv[2].replace(" ",""))
        #system("mkdir {}".format(folder_name))
        #cont = 1
        #for i in playlist:
               #res = popen("youtube-dl -i -x --audio-format mp3 {} -o {}/{:04d}.mp3".format(i,folder_name,cont)).read()
               #print("video {}/{} descargado".format(cont , len(playlist)))
               #cont += 1

        #print("\n"*5)
        #cont = 0



                        #           Imprimo la lista   |mié oct 28 02:59:06 -05 2020|
        cont = 0
        print("playlist:")
        for i in playlist:
            print("{} : {}".format(cont+1 , i))
            cont += 1


        with open("relaciones.md","a+") as f:
            f.write(f"\n## Playlist desde {argv[1]} hasta {argv[2]}\n")
            for c,l in zip(nombres_canciones,playlist):
                f.write(f" - [{c}]({l})\n")







else:
    print("python3 {} <banda1> <banda2> <cantidad temazos por artista>(opcional)".format(argv[0]))

#esto dibuja el path mas corto   |mar oct 27 21:43:34 -05 2020|
#try:
#    nx.draw_networkx(G, pos , node_color = "r" , nodelist = chaman_shortest_path)
#    plt.show()
#except:
#    print("no imprimo nada porque el shortest path no existe")
