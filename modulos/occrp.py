# -------------------------------------------------------------------------------
# Name:        occrp.py
# Purpose:     Módulo OCCRP es una plataforma de información para la investigación
#            
# Author:      IMA
# Contact:     mcint_py@protonmail.com
#
# Created:     20/05/2020
# Copyright:   Copyright (C) 2020 - IMA
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import requests

# Entidad LegalCompany
def company(api_key, company):
    
    parametros = {'Authorization': "ApiKey " + api_key, 'Content-type': "application/json", 'Accept': "application/json"}
    
    r = requests.get("https://aleph.occrp.org/api/2/entities?filter:schemata=LegalEntity&q=" + company,  params=parametros)
    
    try:
        return (__parser(r.json()))
    except Exception:
        return {"error":"Error en OCCRP"}

# Entidad Person
def person(api_key, nombre):
    
    parametros = {'Authorization': "ApiKey " + api_key, 'Content-type': "application/json", 'Accept': "application/json"}
    
    r = requests.get("https://aleph.occrp.org/api/2/entities?filter:schemata=Person&q=" + nombre,  params=parametros)   
   
    try:
        return (__parser(r.json()))
    except Exception:
        return {"error":"Error en OCCRP"}


def __parser(occrp):
   
    dict_occrp = {}
    array_occrp = []

    # Se recorren todos los datos
    for entidad in occrp["results"]:
        
        # Eliminamos los campos no deseados
        e = {k:v for k,v in entidad.items() if k not in ('countries','links','id','score','writeable',
                    'shallow','score''casefile','secret','count','collection')}
        array_occrp.append(e)
        array_occrp.append({"Collection foreign_id": entidad["collection"]["foreign_id"]})
        array_occrp.append({"Collection label": entidad["collection"]["label"]}) 
        array_occrp.append({"Collection summary":entidad["collection"]["summary"]})
       
    # Añadimos el array de datos al diccionario principal
    dict_occrp.update({"results":array_occrp})
   
    return dict_occrp




