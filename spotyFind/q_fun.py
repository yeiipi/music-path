

from bots import *
from os import popen

# global token init | 24.09.2020 | jpi
def init_token():
    global token
    token = get_token()



# retorna el id del artista principal | 18.09.2020 | jpi
def get_varid():
    with open('varid.txt','r') as f:
        return f.read()


# redefine el id del artistas principal | 18.09.2020 | jpi
def nuevo_varid(nv:str):
    with open('varid.txt','w') as f:
        f.write(nv)
        f.close()


# retorna el token de seguridad | 18.09.2020 | jpi
def get_token():
    with open('token.txt','r') as f:
        return f.read()


# redefine el token de seguridad | 18.09.2020 | jpi
def nuevo_token():
    nt = get_tokenb()
    with open('token.txt','w') as f:
        f.write(nt)
        f.close()
    return nt


# query con el json de los artistas relacionados de tipo string | 25.08.2020 | jpi
def get_relacionados(varid,token):
    query = f'curl -X "GET" "https://api.spotify.com/v1/artists/{varid}/related-artists" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {token}"'
    q =  popen(query).read()
    if "The access token expired" in q:
        ntoken = nuevo_token()
        query = f'curl -X "GET" "https://api.spotify.com/v1/artists/{varid}/related-artists" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {ntoken}"'
        q =  popen(query).read()
        print('get_relacionados():Se necesita un nuevo token!!!')
    return q


# query de tipo string con información sobre artista especifico en formato json | 25.08.2020 | jpi
def get_artista(varid,token):
    query = f'curl -X "GET" "https://api.spotify.com/v1/artists/{varid}" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {token}"'
    q =  popen(query).read()
    if "The access token expired" in q:
        ntoken = nuevo_token()
        query = f'curl -X "GET" "https://api.spotify.com/v1/artists/{varid}" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer {ntoken}"'
        q =  popen(query).read()
        print('get_artista():Se necesita un nuevo token!!!')
    return q


