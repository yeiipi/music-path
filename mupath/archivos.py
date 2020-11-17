

import json


# crear diccionarios que relacionan un artista con otros | 17.09.2020 | jpi
def nueva_relación(desde:str,hasta:str):
    return {
        'source': desde,
        'target': hasta
    }


# crea diccionarios con la información necesaria para cada banda individual | 22.09.2020 | jpi
def nueva_banda(ID:str,nombre:str,img_url:str,popularidad:int,seguidores:int,generos:list):
    return {
        'id':ID,
        'nombre':nombre,
        'img_url':img_url,
        'popularidad':popularidad,
        'seguidores':seguidores,
        'generos':generos
    }


# Manda la info con las relaciones de un artista a un archivo json | 23.09.2020 | jpi
def mandalo_para_el_json(c:int,data:dict,v:str):
    fileN = f"{v}"
    fileN = fileN.replace(" ","")
    with open(f'../relaciones/{fileN}_r{c}.json','w') as fa:
        json.dump(data,fa,indent=4,sort_keys=True)






