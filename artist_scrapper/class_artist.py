from os import system
import json
from time import sleep
from os import popen
import pandas as pd


#hace el query para retornar el archivo   |jue ago 13 18:04:45 -05 2020|rcc
def search_result(varid , token):
    command = 'curl -X "GET" "https://api.spotify.com/v1/artists/{}/related-artists" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {}"'.format(varid,token)
    result = popen(command).read()
    return(result)


#lee un archivo de texto y lo interpreta como json   |jue ago 13 18:03:58 -05 2020|rcc
def read_json(json_data):
    return json.loads(json_data)


#lee va a la url y ejecuta el query, retorna un json con los elementos   |jue ago 13 18:04:14 -05 2020|rcc
def read_data(varid , token):
    info = search_result(varid,token)
    elem = read_json(info)
    return(elem['artists'])


#recibe un string de una categoría y retorna toda la lista de la categoria   |jue ago 13 18:28:57 -05 2020|rcc
def full_list(varid , token , string ):
    lista = []
    elem =  read_data(varid , token)
    for i in elem:
        lista.append(i[string])
    return(lista)


#recibe el id de un artista, el token y retorna una lista por cada elemento que nos interesa   |jue ago 13 18:42:32 -05 2020|rcc
class Related_Artists :
    def __init__(self, artist_id , token ,name, father):
        self.id = artist_id
        self.followers = full_list(artist_id , token , 'followers')
        self.images = full_list(artist_id , token , 'images')
        #WARNING la palabra name puede ser confundida con names   |jue ago 13 19:10:29 -05 2020|rcc
        self.names = full_list(artist_id , token , 'name')
        self.genres = full_list(artist_id , token , 'genres')
        self.popularity = full_list(artist_id , token , 'popularity')
        self.ids = full_list(artist_id , token , 'id')
        self.father =  father
        self.name = str(name)


def test():
    #global info   |jue ago 13 18:05:06 -05 2020|rcc
    varid = "06HL4z0CvFAxyc27GXpf02"
    token = "BQB2OdxgjWfnho-4lAkPMbOCNRZxxAgIyVFJuLz5FzR9YpC-CFTBHoYWA8mJHlSSb5YZk9b1WXSRosvRHdsVg_GL0xkFgslLOqmNyoQV3YDmmXL7mhrprLTu7HwBT6dSPGiObkLz55hke1FRj1RhGMNoXuWmX5w"
    art = Related_Artists(varid , token ,None, None )
    artista1 = Related_Artists(art.ids[3] , token,  art.name[3],  art.id)
    


    



test()







