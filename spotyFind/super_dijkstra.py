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


path = "../relaciones/DaftPunk_r2.json"
if((len(argv)== 3)):
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
            print(lista_nombres)
    except:
        print("no se puede hacer dikstra entre esas dos bandas, puede que una de las dos no esté en los datos")


            #Parte grafica:   |mar oct 27 22:20:20 -05 2020|

    #pos = nx.spring_layout(G)  # positions for all nodes
    #nx.draw_networkx(G, pos , node_color = "r"  )
    #plt.show()
    #nx.draw_networkx(G, pos , node_color = "r" , nodelist = chaman_shortest_path)
    #plt.show()
else:
    print("python3 {} <banda1> <banda2>".format(argv[0]))

#esto dibuja el path mas corto   |mar oct 27 21:43:34 -05 2020|
#try:
#    nx.draw_networkx(G, pos , node_color = "r" , nodelist = chaman_shortest_path)
#    plt.show()
#except:
#    print("no imprimo nada porque el shortest path no existe")
