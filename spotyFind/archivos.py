

import json


# crear diccionarios que relacionan un artista con otros | 17.09.2020 | jpi
def relacionar(desde:str,hasta:str):
    return {
        'source': desde,
        'target': hasta
    }


def nueva_banda(ID:str,nombre:str,img_url:str,popularidad:int,generos:list):
    return {
        'id':ID,
        'nombre':nombre,
        'img_url':img_url,
        'popularidad':popularidad,
        'generos':generos}


# crea archivos de listado de bandas + listado de relaciones | 18.09.2020 | jpi
def mandalo_para_el_json(c:int,id_:set,inf_:list,con_:list,v:str):
    fileN = f"{v}"
    fileN = fileN.replace(" ","")
    with open(f'relaciones/{fileN}__id_{c}.json','w') as fa:
        json.dump(list(id_),fa,indent=4)

    with open(f'relaciones/{fileN}_inf_{c}.json','w') as fb:
        json.dump(inf_,fb,indent=4)

    with open(f'relaciones/{fileN}_con_{c}.json','w') as fc:
        json.dump(con_,fc,indent=4)
