# -------------------------------------------------------------------------------
# Name:        hunter.py
# Purpose:     Módulo Hunter encuentra correos asociados a un dominio
#            
# Author:      IMA
# Contact:     mcint_py@protonmail.com
#
# Created:     20/05/2020
# Copyright:   Copyright (C) 2020 - IMA
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests
import json

def analyce(api_key, domain):

    # Se hace la petición a email hunter
    r = requests.get("https://api.hunter.io/v2/domain-search?domain="+domain+"&api_key="+api_key)
    correos = r.json()

    try:
        return (__parser(correos))
    except Exception:
        return {"error":"Error en Hunter"}

def __parser(mails):
    # Diccionario principal donde se almacenarán todos los diccionarios generados por cada email
    dict_mails = {}

    # Añadimos el campo del nombre de la organización
    dict_mails.update({"organization":mails["data"]["organization"]})

    # Array donde se guardará una lista de todos los correos encontrados
    array_mails = []

    # Se recorren todos los correos
    for email in mails["data"]["emails"]:
        
        # Por cada email se genera un diccionario
        dict_mail = {}
        
        # Eliminamos los campos None
        res = {k:v for k,v in email.items() if v is not None}
        dict_mail.update(res)

        sources = []
        # Añadimos la url de las fuentes de donde se ha sacado la información
        for source in email["sources"]:
            sources.append(source["uri"])
        
        dict_mail.update({"sources":sources})

        # Añadimos este correo al array de correos
        array_mails.append(dict_mail)

    # Añadimos el array de correos al diccionario principal
    dict_mails.update({"emails":array_mails})
   
    return dict_mails