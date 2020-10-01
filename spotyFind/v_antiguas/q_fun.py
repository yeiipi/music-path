

from bots import *
from os import popen
from spoty import *
import json

# Client Secret | 01.10.2020 | jpi
es_un_secreto = "1cb6ec606ac048289a3bff4be7895f29"
# Client ID | 01.10.2020 | jpi
esta_si_tranqui = "c12d5ca9e15e433298368cbf94a280a4"

spotify = SpotApi(esta_si_tranqui,es_un_secreto)


# retorna el token de seguridad | 18.09.2020 | jpi
def get_token():

    global spotify

    return spotify.obtener_token()

def get_spot():
    global spotify
    return spotify


# query con el json de los artistas relacionados de tipo string | 25.08.2020 | jpi
def get_relacionados(varid):
    query = f'curl -X "GET" "https://api.spotify.com/v1/artists/{varid}/related-artists" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {get_token()}"'
    q =  popen(query).read()
    return json.loads(q)


# query de tipo string con información sobre artista especifico en formato json | 25.08.2020 | jpi
def get_artista(varid):
    query = f'curl -X "GET" "https://api.spotify.com/v1/artists/{varid}" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {get_token()}"'
    q =  popen(query).read()
    return json.loads(q)


