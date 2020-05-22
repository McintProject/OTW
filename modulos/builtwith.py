# -------------------------------------------------------------------------------
# Name:         builtwith.py
# Purpose:      The BuiltWith Free API provides last updated and counts for
#               technology groups and categories for websites
#              
# Author:      IMA
# Contact:     mcint_py@protonmail.com
#
# Created:     20/05/2020
# Copyright:   Copyright (C) 2020 - IMA
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests

#The Free API will respond with a document in the format -
# result->groups[group->categories[category]] 

def analyze(api_key, domain):
      
    r = requests.get("https://api.builtwith.com/free1/api.json?KEY=" + api_key + "&LOOKUP=" + domain)
    tech = r.json()

    try:
        return(__parser(tech))
    except Exception:
        return {"error":"Error en Builtwith"}
   
def __parser(resp):

    # Diccionario principal
    dict_builtwith = {}
    dict_builtwith.update({"dominio":resp["domain"]})
    
    # Lista de todos los grupos
    array_grupos = []
    for grupo in resp["groups"]:

        # Por cada grupo se genera un diccionario
        dict_grupo = {}
        dict_grupo.update({"group":[grupo["name"]]})
        
        # Listado de categorias por grupo
        categorias = []
        
        for cat in grupo["categories"]:
            categorias.append(cat["name"])
        
        # Guardamos el listado de categorias en cada grupo
        dict_grupo.update({"categories":categorias})
        # Guardamos el grupo en el listado de grupos
        array_grupos.append(dict_grupo) 

    # Guardamos el listado de grupos en el diccionario principal
    dict_builtwith.update({"grupos":array_grupos})

    return  dict_builtwith

