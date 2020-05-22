# -------------------------------------------------------------------------------
# Name:        fullcontact.py
# Purpose:     Módulo FullContact proporciona información adicional de un correo,  
#              teléfono o dominio.
#
# Author:      IMA
# Contact:     mcint_py@protonmail.com
#
# Created:     20/05/2020
# Copyright:   Copyright (C) 2020 - IMA
# Licence:     GNU V3
# -------------------------------------------------------------------------------

import json
import urllib.request

def email(api_key, email):
    
    data = json.dumps({"email": email})
    req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich', data = bytes(data.encode("utf-8")), method = "POST")
    req.add_header('Authorization','Bearer ' + api_key)
    
    try:
        resp = urllib.request.urlopen(req)
        r = json.loads(resp.read().decode("utf-8"))
        res = {k:v for k,v in r.items() if v is not None}
        return res
    except urllib.error.HTTPError as e:
        return str(e)

def phone(api_key, phone):
    
    data = json.dumps({
     "phone": phone
    })
   
    req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich', data = bytes(data.encode("utf-8")), method = "POST")
    req.add_header('Authorization','Bearer ' + api_key)
   
    try:
        resp = urllib.request.urlopen(req)
        r = json.loads(resp.read().decode("utf-8"))
        res = {k:v for k,v in r.items() if v is not None}
        return res
    except urllib.error.HTTPError as e:
        return str(e)

def domain(api_key,domain):
        
    data = json.dumps( {
    "domain": domain
    })
    req = urllib.request.Request('https://api.fullcontact.com/v3/company.enrich', data = bytes(data.encode("utf-8")), method = "POST")
    req.add_header('Authorization','Bearer ' + api_key)
    
    try:
        resp = urllib.request.urlopen(req)
        r = json.loads(resp.read().decode("utf-8"))
        res = {k:v for k,v in r.items() if v is not None}
        return res
    except urllib.error.HTTPError as e:
        return str(e)
